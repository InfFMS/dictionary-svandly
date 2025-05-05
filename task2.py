# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".

numbers = input()

number_massive = numbers.split()

number_massive = list(map(int, number_massive))

print(number_massive)

chetnost = []


for i in number_massive:
    if i % 2 == 0:
        chetnost = chetnost + ["четное"]
    else:
        chetnost = chetnost + ["нечетное"]

print(chetnost)

dictionary = dict(zip(number_massive, chetnost))

print(dictionary)