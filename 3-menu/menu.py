menu = input("Выберите категорию блюда: напиток, суп, десерт - ")

if menu == "напиток":
    print("чай, кофе, сок")
    order = input("Выберите напиток: ")
    match order:
        case "чай":
            print(order, "стоит 50 рублей")
        case "кофе":
            print(order, "стоит 70 рублей")
        case "сок":
            print(order, "стоит 100 рублей")
        case _:
            print("Такого напитка нет в меню")
elif menu == "суп":
    print("борщ, щи, суп-пюре")
    order = input("Выберите суп: ")
    match order:
        case "борщ":
            print(order, "стоит 150 рублей")
        case "щи":
            print(order, "стоит 120 рублей")
        case "суп-пюре":
            print(order, "стоит 170 рублей")
        case _:
            print("Такого супа нет в меню")
elif menu == "десерт":
    print("торт, мороженое, фрукты")
    order = input("Выберите десерт: ")
    match order:
        case "торт":
            print(order, "стоит 150 рублей")
        case "мороженое":
            print(order, "стоит 120 рублей")
        case "фрукты":
            print(order, "стоит 170 рублей")
        case _:
            print("Такого десерта нет в меню")