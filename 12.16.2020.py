# n1 = input()
# n2 = input()
# if 'a' in n1 or 'c' in n1 or'e' in n1 or'g' in n1:
#     if '1' in n1 or '3' in n1 or'5' in n1 or'7' in n1:
#        n1 = False
#     else:
#        n1 = True
# elif 'b' in n1 or 'd' in n1 or'f' in n1 or'h' in n1:
#     if '2' in n1 or '4' in n1 or'6' in n1 or'8' in n1:
#        n1 = False
#     else:
#        n1 = True
# if 'a' in n2 or 'c' in n2 or 'e' in n2 or 'g' in n2:
#     if '1' in n2 or '3' in n2 or '5' in n2 or '7' in n2:
#         n2 = False
#     else:
#         n2 = True
# elif 'b' in n2 or 'd' in n2 or 'f' in n2 or 'h' in n2:
#     if '2' in n2 or '4' in n2 or '6' in n2 or '8' in n2:
#         n2 = False
#     else:
#         n2 = True
# if n1==n2:
#     print("YES")
# else:
#     print('NO')

# ____________________________________________________________________
# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».
#
# Sample Input 1:
#
# 2000
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 1999
# Sample Output 2:
#
# NO


#
# n = int(input())
# # print(n%10)
# # print(n//10%10)
# if n%10 == 0  and n//10%10 == 0:
#     print("YES")
# else:
#     print("NO")
#
# ___________________________________________________________________

# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

# Sample Input 1:
#
# 1
# 1
# 2
# 6
# Sample Output 1:
#
# YES


# n1 = int(input())
# n2 = int(input())
# b1 = int(input())
# b2 = int(input())
# a = ''
# b = ''
# if n1 == 1 or n1 == 3 or n1 == 5 or n1 == 7:
#     if n2 == 1 or n2 == 3 or n2 == 5 or n2 == 7:
#        a = "white"
#     else:
#        a = "black"
# elif n1 == 2 or n1 == 4 or n1 == 6 or n1 == 8:
#     if n2 == 2 or n2 == 4 or n2 == 6 or n2 == 8:
#        a = "white"
#     else:
#        a = "black"
# if b1 == 1 or b1 == 3 or b1 == 5 or b1 == 7:
#     if b2 == 1 or b2 == 3 or b2 == 5 or b2 == 7:
#        b = "white"
#     else:
#        b = "black"
# elif b1 == 2 or b1 == 4 or b1 == 6 or b1 == 8:
#     if b2 == 2 or b2 == 4 or b2 == 6 or b2 == 8:
#        b = "white"
#     else:
#        b = "black"
# if a == b:
#     print("YES")
# else:
#     print('NO')

# _________________________________________________
# Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. Если претендент подходит, то выведите «YES», иначе выведите «NO».
#
# Формат входных данных
# На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).

# a = int(input())
# b = input()
# if 10 <= a <= 15  and b == "f":
#     print('YES')
# else:
#     print("NO")


# _________________________________________________________
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
#
# В таблице приведены римские цифры для чисел от 1 до 10.

# n = int(input())
# a = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
# if 1 <= n <=10:
#     print(a[n-1])
# else:
#     print("ошибка")

# _______________________________________________________

# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

# n = int(input())
# if n%2 != 0:
#    print("YES")
# elif n%2 == 0:
#     if 2 <= n <= 5:
#        print("NO")
#     elif 6 <= n <= 20:
#        print("YES")
#     elif n > 20:
#        print("NO")


# ____________________________________________________________
#
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
#     print('YES')
# elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
#     print('YES')
# else:
#     print("NO")

# _________________________________________
#
# Программа принимает на вход три символа через пробел в одну строку. Необходимо вывести код каждого символа при помощи функции ord в определенном формате.


# a, c, b =map(str,input().split())
# print(f'Simvol code {a} is {ord(a)}.')
# print(f'Simvol code {c} is {ord(c)}.')
# print(f'Simvol code {b} is {ord(b)}.')

# ________________________________________________
#
# Напишите программу, которая считывает целое число, и затем сообщает какие числа будут следующим и предыдущим в определенном формате. Пробелы, знаки препинания, заглавные и строчные буквы важны!
#
# Sample Input:
#
# 99
# Sample Output:
#
# Для числа 99 предыдущим будет число 98.
# Для числа 99 следующим будет число 100.

# n = int(input())
# print(f"Для числа {n} предыдущим будет число {n-1}.")
# print(f"Для числа {n} следующим будет число {n+1}.")
#
# ______________________________________________________
# Напишите программу для перевода натурального значения секунд в значение минут определенного формата.
#
# Sample Input 1:
#
# 99
# Sample Output 1:
#
# 99 сек - это 1 мин. 39 сек.

# n = int(input())
# print(f'{n} сек - это {n//60} мин. {n%60} сек.')
#
# ________________________________________________________
# Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. В результате на экране разрешение экрана и общее количество пикселей в определенном формате. Все знаки препинания, пробелы, регистр букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»
#
# Sample Input:
#
# 1920 1080
# Sample Output:
#
# Разрешение экрана: 1920 x 1080.
# Общее количество пикселей = 2073600.

# ____________________________________________________________
# Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. В результате на экране разрешение экрана и общее количество пикселей в определенном формате. Все знаки препинания, пробелы, регистр букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»
#
# Sample Input:
#
# 1920 1080
# Sample Output:
#
# Разрешение экрана: 1920 x 1080.
# Общее количество пикселей = 2073600.

# a, b = map(int, input().split())
# print(f'Разрешение экрана: {a} x {b}.')
# print(f'Общее количество пикселей = {a * b}.')
#
# ______________________________________________________________
# Нашей программе поступает на вход x, y, z - три целых числа, обозначающие координаты вектора А. Затем необходимо найти координаты вектора B, путем увеличения на 5 каждой из координаты вектора А.
# #
# # Оба вектора необходимо распечатать в определенном формате
# #
# # Sample Input 1:
# #
# # 1
# # 2
# # 3
# # Sample Output 1:
# #
# # Vector A(1, 2, 3)
# # Vector B(6, 7, 8)

# a, b, c = int(input()), int(input()), int(input())
# print(f'Vector A({a}, {b}, {c})')
# print(f'Vector A({a + 5}, {b + 5}, {c + 5})')

# ________________________________________________

# Допишите программу ниже, чтобы она вывела через пробел в одной строке значения самого маленького и самого большого элементов списка my_list.

#
# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# print(min(my_list), max(my_list))
#
# ___________________________________________________

# n, m =map(int, input().split())
# answer = n + (n - 1) // (m - 1)
# print(answer)
# ________________________________________________________
#
# Пользователь вводит целые числа по одному в строке, последовательность оканчивается числом 0. Все, что вводится после 0 не относится к последовательности. Напишите программу, которая выводит сумму всех членов данной последовательности.
#
# Sample Input 1:
#
# 1
# 2
# 3
# 0
# 5
# 6
# Sample Output 1:
#
# 6

# n = int(input())
# s = 0
# count = -1
# while s <= n:
#     a=s
#     count += 1
#     n1 = int(input())
#     s += n1
# print("Довольно!")
# print(a)
# print(count)
# _______________________________________________________
# Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду. Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик, на втором уровне — 1 + 2 = 3 кубика, на третьем — 1 + 2 + 3 = 6 кубиков, и так далее. Таким образом, на i-м уровне пирамиды должно располагаться 1 + 2 + ... + (i - 1) + i кубиков.
# n = int(input())
# used_cubers = 0
# cubes_in_row = 0
# row = 0
# while used_cubers <= n:
#     row +=1
#     cubes_in_row = cubes_in_row + row
#     used_cubers += cubes_in_row
# print(row -1)

# _______________________________________________
from math import *

# n, m = map(int, input().split())
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
# list3 = list1 + list2
# print(*sorted(list3))
#
# _________________________________________________
# Программа получает на вход натуральное число n > 1. Выведите минимальный делитель этого числа, отличный от единицы.
#
# К примеру для числа 12 делителями являются 1, 2, 3, 4, 6, 12.
#
# Sample Input 1:
#
# 12
# Sample Output 1:
#
# 2
#
# n = int(input())
# a = []
# for i in range(1,n+1):
#     if n % (i) == 0:
#         if i == 1:
#             continue
#         a.append(i)
# print(min(a))

# _______________________________________________________
# Давайте переберем все числа от а до b включительно и будем их выводить на экран, при этом нужно выполнить следующие условия:
#
# пропускать (не выводить) числа, которые делятся на 2 или на 3
# если встречаете число, кратное 777, необходимо принудительно закончить цикл, само это число не выводить

# n1, n2  = int(input()), int(input())
# n1 = n1 - 1
# while n1 < n2 :
#     n1 +=1
#     if n1 == 777:
#          break
#     if n1 % 2 == 0:
#          continue
#     if n1 % 3 == 0:
#          continue
#     print(n1)

# ________________________________________________________
#
# Вам на вход поступает слово и ваша задача в цикле while обойти все его буквы и распечатать их в формате фразы:
#
# «Текущая буква: <letter>».
#
# Как только вы встретите строчные английские буквы «e» или «a» нужно вывести фразу «Ага! Нашлась», перестать печатать буквы и принудительно выйти из цикла.
#
# В случае, если в слове не оказалось букв «e» или «a» необходимо вывести фразу «Распечатали все буквы»
#
# Sample Input 1:
#
# phrase
# Sample Output 1:
#
# Текущая буква: p
# Текущая буква: h
# Текущая буква: r
# Ага! Нашлась
#
# n = input()
# i=0
# while len(n) != i:
#     if n[i] == 'e' or n[i] == 'a':
#         print('Ага! Нашлась')
#         break
#     print(f'Текущая буква: {n[i]}')
#     i+=1
# else:
#     print('Распечатали все буквы')
# # ________________________________________________________



# На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит натуральное число из отрезка [a; \, b][a;b] с максимальной суммой делителей.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.

# a, b = int(input()), int(input())
# counter = 0 # счетчик подсчета суммы делителей
# number = 1 # число которое будем выводить (минимум 1)
# summa = 0  # тут будет сумма делителей, которую надо будет вывести
# for i in range(a, b + 1):  # проверяем каждое число в [a;b]
#     counter = 0 # обнуляем счетчик для каждого i
#     for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
#         if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
#             counter += j  # создаем сумму делителей
#     if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
#         summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
#         number = i  # число у которого делителей оказалось больше, теперь равно number
# print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей
#
# _____________________________________________________
# Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.
#
# Формат входных данных
# На вход программе подается одно натуральное число.

# import math
# n = int(input())
# sum_factorial = 0
# for i in range(1, n +1):
#     sum_factorial += math.factorial(i)
# print(sum_factorial)
# _______________________________________________________
# На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. В случае, если положительных значений нет, выведите строку "Empty"
#
# Sample Input 1:
#
# 8 11 -9 0 5 -20
# Sample Output 1:
#
# 5
#
#
# a= list(map(int,input().split()))
# b=[]
# for i in range(len(a)):
#     if a[i]>0:
#         b.append(a[i])
# if len(b)<=0:
#     print("Empty")
# else:
#     print(min(b))
# __________________________________________________________

# lst=[]
# count=1
# for i in range(4):
#     lst.append(input())
# for i in lst:
#     print(i)
# for i in range(4):
#     for j in range(4):
# #         print([i][j], end=' ')
# #     print()
#         if lst[i][j] == lst[i+1][j] == lst[i][j+1] == lst[i+1][j+1]:
#             print('No')
#             break
#         else:
#             print('Yes')


# ________________________________________________________
# Вывести список, содержащий нечетные натуральные числа в интервале  [ nn; n^2n
# 2
#   ]
#
# Sample Input 1:
#
# 7
# Sample Output 1:
#
# [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# n = int(input())
#
# b = [i for i in range(n, n**2 + 1) if i % 2 != 0]
# print(b)
# ____________________________________________________
#
# Создайте список первых букв каждого слова из строки st и выведите его на экран
# st = 'Create a list of the first letters of every word in this string'
#
# b=st.split()
#
# t = [b[i][0] for i in range(len(b))]
# print(t)
# ____________________________________________________
# При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'. Слова возьмите из переменной phrase, также не забывайте про метод split()
#
# В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке, в котором они стояли в изначальной фразе
# phrase = 'Take only the words that start with t in this sentence'
#
# phrase = 'Take only the words that start with t in this sentence'
# print([i for i in phrase.split() if i[0] in 't' or i[0] in 'T'])

# ______________________________________________________
# На вход программе подается четное число n, \, n \ge 2n,n≥2. Напишите программу, которая выводит список четных чисел
#
#  [2, 4, 6, ..., n].
#
#
# n = int(input())
# print([i for i in range(2, n +1) if i % 2 == 0])

# ______________________________________________________

# На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие целые числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# n1 = list(map(int, input().split()))
# n2 = list(map(int, input().split()))
# a =[]
# for i in range(len(n1)):
#     a.append(n1[i] + n2[i])
# print(*a)
# ---------
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# print(*[x + y for x, y in zip(a, b)])

# _________________________________________________________
# На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.


# n = list(map(int, input().split()))
# s = 0
# for i in range(len(n)):
#     s += int(n[i])
# print(*n, sep='+', end='=')
# print(s)

# ________________________________________________________
#
# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:
#
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

# n = input().split("-")
# c = [len(i) for i in n]
# if c == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")
#
# ______________________________________________
#
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.
#
# Формат входных данных
# На вход программе подается строка текста.

# n = input().split()
# c = [len(i) for i in n]
# print(max(c))

# __________________________________________
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу:
#
# первая буква каждого слова удаляется и ставится в конец слова;
# затем в конец слова добавляется слог "ки".
# Формат входных данных
# На вход программе подается строка текста на русском языке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# n = input().split()
# print(*([i[1:] + i[0] + 'ки' for i in n]))
# _______________________________________________

# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 7 != 0:
#         counter += 1
# print(counter)

# Дано натуральное число. Напишите программу, которая вычисляет:
# n = input()
# number3 = 0
# last = n[-1]
# lastnumber = 0
# coun=0
# more5 = 0
# more7 = 1
# howmany05 = 0
# for i in n:
#     if i in '3':
#         number3 +=1
#     if i in last:
#         lastnumber +=1
#     if int(i)%2==0:
#         coun +=1
#     if int(i)>5:
#        more5 +=int(i)
#     if int(i)>7:
#        more7 *=int(i)
#     if int(i) == 0 or int(i) ==5:
#       howmany05 +=1
#
#
# print(number3)
# print(lastnumber)
# print(coun)
# print(more5)
# print(more7)
# print(howmany05)

# ______________________________________________________
# city = input()
# flag = 0
# for key, value in countries.items():
#     if city in value:
#         flag +=1
#         print(f'INFO: {city} is a city in {key}')
#     else:
#         continue
# if flag==0:
#     print(f'ERROR: Country for {city} not found')
#
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }

city = input()
flag = 0
for key, value in countries.items():
    if city in value:
        flag +=1
        print(f'INFO: {city} is a city in {key}')
    else:
        continue
if flag==0:
    print(f'ERROR: Country for {city} not found')

