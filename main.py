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

user_year = int(input("Введите год:   "))
print("YES" if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0) else "NO")