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










#семинар 4 _______________________________________________________________________________________________
# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# arr = "a a a b c a a d c d d".split(" ")
# result_arr = []
#
# for index_chr in range(len(arr) - 1):
#     count = arr[:index_chr].count(arr[index_chr])
#     result_arr.append(f"{arr[index_chr]}_{count}" if count > 0 else f"{arr[index_chr]}")
# print(" ".join(result_arr))

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13


# user_text = input('Enter text:   ')
# print(len(set(user_text.split(" "))))

# subsequence = [random.randint(0, 100) for i in range(int(input('count:  ')))]
# print(subsequence)
# max_element = 0
# for item in subsequence:
#     if item > max_element:
#         max_element = item
#     if item == 0:
#         break
# print(max_element)

#print(max(subsequence) if (0 in subsequence) == False else max(subsequence[:subsequence.index(0)]))


def is_prime_number(number):
    res_arr = [i for i in range(1, number + 1) if number % i == 0]
    print(res_arr)
    return "YES" if len(res_arr) == 2 else "NO"
def revers_input(user_count):
    x = input("enter number:   ")
    if user_count != 1:
        revers_input(user_count - 1)
    print(x)

#revers_input(int(input('enter count:  ')))


# n = int(input('введите N-e число:   '))
# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
# print(fib(n))

def fib(n):
    res = 1
    if n < 2:
        return 1
    else:
        res = fib(n - 1) + fib(n - 2)
        return res

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

def del_all_max_value(arr):

    return ", ".join([str(i) for i in arr]).replace(str(max(arr)), str(min(arr)) )

#arr_numbers = [int(input("enter number:   ")) for i in range(3)]
#print(del_all_max_value(arr_numbers))

#семинар 6
#first_numbers_arr = [int(input('enter digit:   ')) for i in range(int(input('enter count first array:   ')))]
#second_numbers_arr = [int(input('enter digit:   ')) for i in range(int(input('enter count second array:   ')))]

# Задача No39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#1
# print(list(filter(lambda x: x not in second_numbers_arr, first_numbers_arr)))
# #2
# arr_res = [i for i in first_numbers_arr if i not in second_numbers_arr]


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
# элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


# user_array = [int(input('enter digit:   ')) for i in range(int(input('enter count:    ')))]
# def not_name(arr):
#     count_el = 0
#     for index in range(1, len(arr) - 1):
#         if arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
#             count_el += 1
#     return count_el
#
#
# print(not_name(user_array))

# Задача No43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
#
# arr = [1, 2, 3, 2, 5, 1]
# print(len(arr) - len(set(arr)) if ((len(arr) - len(set(arr))) % 2) == 0 else len(arr) - len(set(arr)) - 1)


# Задача No45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая
# само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
# дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
# не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только
# один раз (перестановка чисел новую пару не дает).

# number = int(input('enter digit:   '))
# for num1 in range(1, number):
#     arr_del_1 = [i for i in range(1, num1) if num1 % i == 0]
#     for num2 in range(num1, number):
#         arr_del_2 = [i for i in range(1, num2) if num2 % i == 0]
#         if sum(arr_del_1) == num2 and sum(arr_del_2) == num1:
#             print(num1, num2, sep= " ", end= "||")

