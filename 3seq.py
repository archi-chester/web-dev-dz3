"""
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Будут удалены по одному экземпляру каждого из совпадающих элементов
"""
#   получаем значения списков
first_list_of_digits = input("Введите список цифр, разделенных запятой: ").split(",")
second_list_of_digits = input("Введите список цифр, разделенных запятой: ").split(",")
#   перегоняем в набор
uniq_1st_set_of_digits = set(first_list_of_digits)
uniq_2st_set_of_digits = set(second_list_of_digits)
items_in_both_lists = uniq_1st_set_of_digits.intersection(uniq_2st_set_of_digits)
#   удаляем из списка пересекающиеся значения
for digit in items_in_both_lists:
    #   убиваем все вхождения
    while digit in uniq_1st_set_of_digits:
        uniq_1st_set_of_digits.remove(digit)
#   перегоняем в строку с разделителями
string_of_uniq_digits = ", ".join(uniq_1st_set_of_digits)
#   выводим
print(f"Результат: {string_of_uniq_digits}")
