
import sys

choosen_method = sys.argv[1]
filter_option = sys.argv[2]

books = {"Евгений Онегин": "Пушкин", "Капитанская дочка": "Пушкин", "Руслан и Людмила": "Пушкин",
         "Шурале": "Тукай", "Водяная": "Тукай", "Сказка о козе и баране": "Тукай"}

if choosen_method == "filter":
    filtered = dict(
        filter(lambda item: item[1] == filter_option, books.items()))

    print(list(map(lambda item: f"{item[0]} - {item[1]}", filtered.items())))


else:
    formatted_list = list(
        map(lambda item: f"{item[0]} — {item[1]}", books.items()))

    if choosen_method == "sort" and filter_option == "author":
        sorted_by_author = sorted(
            formatted_list, key=lambda x: x.split(" — ")[1])
        print(sorted_by_author)
    elif choosen_method == "sort" and filter_option == "book":
        sorted_by_book = sorted(
            formatted_list, key=lambda x: x.split(" — ")[0])
        print(sorted_by_book)
