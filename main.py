# This is a sample Python script.
import random

words_array = ["луна", "солнце", "машина", "ноутбук", "цветок", "дерево", "давление", "сотрудник"]
secret_word = random.choice(words_array)
print(f"случайное слово содержит {len(secret_word)} слов")
print("Угадайте загаданное слово")
startX = "_" * len(secret_word)
print(startX)
flag = True
while flag:
    user_letter = input("введите букву:   ")
    if user_letter in secret_word:
        print(f"вы угадали букву {user_letter}")
        for item in enumerate(secret_word):
            if item[1] == user_letter:
                startX = startX[:item[0]] + user_letter +startX[item[0] + 1:]
        print(startX)
    if startX == secret_word:
        print("Win!!!!!")
        flag = False



