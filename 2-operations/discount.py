price = int(input("Введите стоимость товара: "))
discont = int(input("Введите размер скидки: "))

total = price - (discont * price / 100)

print("Окончательная стоимость товара: ", total)