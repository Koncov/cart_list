"""
Корзина товаров.
Каждый товар, это заголовок, картинка, цена, количество, отмечено.
"""
products = [
    ['батон хлеба', 'baton.jpg', 60, 2, False],
    ['микроволновая печь', 'microvolnovka.jpg', 4000, 1, True],
    ['чесалка для головы', 'chesalka.jpg', 700, 3, True],
    ['велосипед', 'velosiped.jpg', 6000, 1, False],
]

command = input("Введите текст команды: ")
while command != "выход":
    if command == "количество":
        index = int(input("Введите номер продукта: ")) - 1
        products[index][3] = int(input("Ведите новое количество: "))

    elif command == "отметка":
        index = int(input("Введите номер продукта: ")) - 1
        if products[index][4]:
            products[index][4] = False
        else:
            products[index][4] = True

    elif command == "оформить":
        print("Название", "Изображение", "Цена", "Количество", "Стоимость", "Отмечено", sep=" || ")
        itogo = 0
        for product in products:
            if product[4]:
                summa = product[2] * product[3]
                itogo += summa
                print(product[0], product[1], product[2], product[3], summa, product[4], sep=" || ")
        print(f"Итого к оплате - {itogo} руб.")
        otvet = input("Подтвердить оплату \"да\\нет\" :")
        if otvet == "да":
            for i in range(len(products) - 1, -1, -1):
                if products[i][4]:
                    products.pop(i)
            print(f"Заказ оформлен. Со счета списано {itogo} руб.")
        else:
            print("Отказ от оформления!")

    elif command == "показать":
        print("Название", "Изображение", "Цена", "Количество", "Стоимость", "Отмечено", sep=" || ")
        itogo = 0
        for product in products:
            summa = product[2] * product[3]
            itogo += summa
            print(product[0], product[1], product[2], product[3], summa, product[4], sep=" || ")
        print(f"Итого к оплате - {itogo} руб.")

    else:
        print("Неверная команда!")

    command = input("\n Введите команду: ")

print("\n Корзина закрыта")
