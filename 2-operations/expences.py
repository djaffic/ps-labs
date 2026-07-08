# еда, транспорт, развлечение

meal = int(input("Введите сколько Вы потратили на еду: "))
transport = int(input("Введите свои траты на транспорт: "))
game = int(input("Введите свои траты на развлечения: "))

sum = meal + transport + game

avg = (meal + transport + game) / 3

print("Сумма трат: ", sum)
print("Среднее: ", avg)