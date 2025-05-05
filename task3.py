# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2

import numpy as np

slovo = str(input())

slovo = slovo.lower()

slovo_list = np.array(list(slovo))

print(slovo_list)
counter = 0
znachenia = np.unique(slovo_list)
m = int(0)
massivechisel = []
i = int(0)
print(znachenia)

while m < len(znachenia):
    while i < len(slovo_list):
        if slovo_list[i] == znachenia[m]:
            counter += 1
        i+=1
    massivechisel = massivechisel + [counter]
    counter = 0
    m += 1
    i = int(0)

dictionary = dict(zip(slovo_list, massivechisel))

print(dictionary)




