# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
keys = input()
meaning = input()

keys_massive = keys.split()
meaning_massive = meaning.split()

dictionary = dict(zip(keys_massive, meaning_massive))

print(dictionary)