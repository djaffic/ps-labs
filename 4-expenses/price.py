sum = input("Введите сумму: ").strip()

if len(sum.split()) == 2:
    integer = sum.split()[0]
    if integer.isdigit():
        print(f"{int(integer):.2f} ₽")
elif len(sum.split()) == 4:
    integer = sum.split()[0]
    fractional = sum.split()[2]
    if integer.isdigit() and fractional.isdigit():
        print(f"{integer}.{fractional} ₽")
