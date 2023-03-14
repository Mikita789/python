# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# digit = int(input("Введите трехзначное число:    "))
# one_digit = digit // 100
# two_digit = (digit // 10) % 10
# three_digit = digit % 10
# print(f"Cпособ 1:сумма цифр числа {digit} = {one_digit + two_digit + three_digit}")
# print(f"Способ 2:сумма цифр введенного числа {sum([int(i) for i in input('Введите трехзначное число для способа 2: ')])}")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# count_origami = int(input("Введите общее кол-во поделок:    "))
# x = count_origami / 6
# print(f"Петя сделал {int(x)} {'журавлика' if x <= 4 else 'журавликов'},"
#       f" Сережа сделал {int(x)} {'журавлика' if x <= 4 else 'журавликов'},"
#       f" Катя сделала {int(x * 4)} {'журавлика' if x * 4 <= 4 else 'журавликов'}")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
# digit = input('Введите шестизначный номер билета:   ')
# print("YES" if sum([int(i) for i in digit[:3]]) == sum([int(i) for i in digit[3:]]) else "NO")
#
# #способ 2
# one = int(digit) // 100000
# two = (int(digit) // 10000) % 10
# three = (int(digit)) // 1000 % 10
# four = (int(digit) // 100) % 10
# five = (int(digit) // 10) % 10
# six = int(digit) % 10
# print([one , two, three, four, five, six])
# if one + two + three == four + five + six :
#     print("YES")
# else:
#     print("NO")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
# m = int(input("Введите длину:   "))
# n = int(input("Введите ширину:   "))
# k = int(input("Введите сколько должно остаться:   "))
#
# print("YES" if ((k % m == 0) or (k % n == 0)) and k < m * n else "NO")



#--------------------------------------------------------------------------
#HW 2
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

#1
# coins = [int(input("enter 1(орел) or 0(решка):  ")) for i in range(int(input("enter count coins: ")))]
# print(min(len(list(filter(lambda x: x == 0, coins))), len(list(filter(lambda x: x == 1, coins)))))

#2
# count_nul = 0
# count_one = 0
# count_coins = int(input("enter count coins:  "))
# for x in range(count_coins):
#     coin = int(input("enter 1(орел) or 0(решка):   "))
#     if coin == 1:
#         count_one += 1
#     else:
#         count_nul += 1
# print(count_one if count_one <= count_nul else count_nul)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# s, p = int(input("enter S:  ")), int(input("enter P:  "))
# x, y = 0, 0
# max = s if s > p else p
# flag = True
# for i in range(1, max + 1):
#     if flag == False:
#         break
#     for j in range(1, max + 1):
#         if i + j == s and i * j == p:
#             x = i
#             y = j
#             flag = False
#             break
#
# print(f"x = {x}, y = {y}")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def fetch_int():
    flag = True

    while flag:
        try:
            res = int(input("Enter digit:  "))
            flag = False
        except:
            print("error conv. Repeat! ")

    return res
#1
#max_digit = fetch_int()
# res = 0
# pow = 0
#
# while 2 ** pow < max_digit:
#     res = 2 ** pow
#     pow += 1
#     print(res, end = " ")

#2
import math

# for i in range(int(math.sqrt(max_digit)) + 1):
#     print(2 ** i, end = " ")

#3
print(*[2 ** i for i in range(int(math.sqrt(max_digit)) + 1)])