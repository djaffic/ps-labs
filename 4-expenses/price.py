
while True:
    print("Добавить расход")
    print ("Показать все расходы")
    print("Показать сумму и средний расход")
    print("Удалить расход по номеру")
    print("Выход")
    user_choice = input("Выберите один из вариантов: ")
    if user_choice == "Выход":
        print("Выходим из программы")
        break



# sum = input("Введите сумму: ").strip().lower()

# if len(sum.split()) == 2:
#     integer = sum.split()[0]
#     rub = sum.split()[1]
#     if integer.isdigit() and rub == "руб":
#         print(f"{int(integer):.2f} ₽")
# elif len(sum.split()) == 4:
#     integer = sum.split()[0]
#     rub = sum.split()[1]
#     fractional = sum.split()[2]
#     kop = sum.split()[3]
#     if integer.isdigit() and fractional.isdigit() and rub == "руб" and kop == "коп":
#         if len(fractional) == 1:
#             print(f"{integer}.0{fractional} ₽")
#         elif len(fractional) == 2:
#             print(f"{integer}.{fractional} ₽")
# else:
#     print("Некорректный формат суммы")