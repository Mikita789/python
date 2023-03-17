# This is a sample Python script.
import math
import random

# print("Угадайте загаданное слово")
# words_array = ["луна", "солнце", "машина", "дорога", "цветок", "дерево", "светофор", "автобус", "словарь", "момент", "обувь", "одежда", "штраф", "отпуск", "курорт"]
# secret_word = random.choice(words_array)
# print(f"случайное слово содержит {len(secret_word)} букв")
# startX = "_" * len(secret_word)
# count = 0
# print(startX)
# flag = True
# while flag:
#     user_letter = input("введите букву:   ")
#     count += 1
#     if user_letter in secret_word:
#         print(f"вы угадали букву {user_letter}")
#         for item in enumerate(secret_word):
#             if item[1] == user_letter:
#                 startX = startX[:item[0]] + user_letter +startX[item[0] + 1:]
#         print(startX)
#     if startX == secret_word:
#         print(f"Слово угадано !!!!! {count} попыток")
#         flag = False

# count_part = 0
# count_kl = 3
# for i in range(count_kl):
#     count = int(input(f"Введите число учащихся в классе {i+1}:   "))
#     count_part += math.ceil(count / 2)
#
# print(f"необходимо парт: {count_part}")

# user_year = int(input("Введите год:   "))
# print("YES" if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0) else "NO")








# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# digit = int(input("Enter digit:   "))
# result = 1
# if digit == 0:
#     print(f"factorial = 1")
# else:
#     while digit > 0:
#         result *= digit
#         digit -= 1
#     print(f"Factorial digit({digit}!)    =   {result}")



# Задача No11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# число n,что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.


# digit = int(input("Enter digit :   "))
# a, b = 1, 1
# flag = True
# count = 0
#
# while flag:
#     a, b = b, a + b
#     count += 1
#     if digit == a:
#         print(f"digit {digit} fibo!!! position: {count + 2}")
#         flag = False
#     elif a > digit:
#         print(f"sorry, digit {digit} not fibo :(")
#         flag = False


# Задача No13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые
# годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N
# целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне
# от –50 до 50

# count_day = int(input("Enter count days:  "))
# result_count = 0
# max_days_count = 0
# for temp in range(count_day):
#     user_input = int(input("Enter temperature:   "))
#     if user_input > 0:
#         result_count += 1
#         if result_count > max_days_count:
#             max_days_count = result_count
#     else:
#         result_count = 0
#
# print(f"max days: {max_days_count}")




# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза

# count = int(input("enter count:   "))
#
# max = 0
# min = 1000000
#
# for weight in range(count):
#     m = int(input("Enter weight:   "))
#     if m > max:
#         max = m
#     if m < min:
#         min = m
# print(f"min weight: {min}, max weight: {max}")
# arr = [int(input("Введите массу арбуза:  ")) for i in range(int(input("Введите сколько будет арбузов:  ")))]
# print(f"max = {max(arr)} and index = {arr.index(max(arr))}. min = {min(arr)} and index = {arr.index(min(arr))}")

# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.


# print(f'number of unique values:  {len(set(input("enter elements separated by spaces: ").split(" ")))}')

# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# arr_numbers = [int(i) for i in input("enter elements separated by spaces: ").split(" ")]
# k = int(input('enter K number:  '))
#1
# for index_element in range(len(arr_numbers)):
#     arr_numbers[index_element] += k
# print(*arr_numbers)

#2
#print(*list(map(lambda x: x + k, arr_numbers)))

#print(arr_numbers[k:] + arr_numbers[:k])


# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#         {"VIII":"S007"}]
# print(*set([list(d.values())[0] for d in dict]))

# Задача No23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

# arr_numbers = [int(i) for i in input('enter elements separated by spaces: ').split(" ")]
#1
# count = 0
# for index in range(1, len(arr_numbers)):
#     if arr_numbers[index] > arr_numbers[index - 1]:
#         count += 1
# #2
# print(len([arr_numbers[i] for i in range(1, len(arr_numbers)) if arr_numbers[i] > arr_numbers[i - 1]]))

a = [1,2,3,4]
print("".join(map(lambda x : str(x), a)))


