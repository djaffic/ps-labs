expenses = [100, 200, 300, 400, 500, 600, 700]

expenses_type = ["Добавить расход", "Показать все расходы",
                 "Показать средний расход", "Удалить расход по номеру", "Выход"]


def add_expense(expenses, value):
    """Функция для добавления расходов"""

    expenses.append(value)
    return expenses


def delete_expense(expenses, index):
    """Функция для удаления расхода по индексу"""

    del expenses[index]
    return expenses


def get_total(expenses):
    """Функция для расчета общей суммы расходов"""

    return sum(expenses)


def get_average(expenses):
    """Функция для расчета среднего у расходов"""

    avg = sum(expenses) / len(expenses)
    return avg


def print_report(expenses):
    """Функция для вывода расходов"""

    return f"{expenses} | {get_total} | {get_average}"


print(expenses_type)

while True:
    user_choice = input("Выберите один из вариантов: ")

    match user_choice:
        case "Добавить расход":
            add_expense(expenses, 1000)
            print(expenses)
        case "Удалить расход по номеру":
            delete_expense(expenses, 3)
            print(expenses)
        case "Показать все расходы":
            print(get_total(expenses))
        case "Показать средний расход":
            print(get_average(expenses))
        case "Напечатать отчёт":
            print_report(expenses)
        case _:
            print("Выходим из программы")
            break
