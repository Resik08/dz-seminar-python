# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
# нужно перевернуть


import sys

input_str = input("Введите элементы массива, разделенные пробелами: ")
arr = input_str.split()
arr = [int(x) for x in arr]
nol = 0
odin = 0
for n in arr:
    if n < 0 or n > 1:
        print('Данные не корректны, работа программы завершена')
        sys.exit()
    else:
        if n == 0:
            nol +=1
        else: odin+=1
if nol <= odin: print("{} переворота".format(nol))
else: print("{} переворота".format(odin))


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате
# отгадать задуманные Петей числа.


s = int(input('Задайте сумму двух чисел \n'))
p = int(input('Задайте произведение чисел \n'))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число ="{x}", второе число ="{y}"')


# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: \n'))
i = 0
while 2 ** i <= n:
    print(f' 2 в степени {i} равна {2 ** i}')
    i += 1




