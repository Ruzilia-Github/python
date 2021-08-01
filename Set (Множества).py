# Суммы четвертей
# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
#
#
#
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Элементы диагоналей не учитываются.
#
# Sample Input 1:
#
# 4
# 1 2 3 4
# 5 6 7 8
# 3 4 5 6
# 1 2 3 4
# Sample Output 1:
#
# Верхняя четверть: 5
# Правая четверть: 14
# Нижняя четверть: 5
# Левая четверть: 8

# n = int(input())
# mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
# print('Верхняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)]))
# print('Правая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)]))
# print('Нижняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)]))
# print('Левая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)]))

# Таблица умножения
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
#
# Формат входных данных
# На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте строковый метод ljust()).
#
# Sample Input 1:
#
# 4
# 6
# Sample Output 1:
#
# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8  10
# 0  3  6  9  12 15

# n, m = int(input()), int(input())
# for i in range(n):
#     for j in range(m):
#         print(str(i*j).ljust(3), end=' ')
#     print()

# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
#
# Sample Input 1:
#
# 4
# 1 2 3 4
# 5 6 7 8
# 8 6 4 2
# 3 4 5 6
# Sample Output 1:
#
# 3 4 5 6
# 8 6 4 2
# 5 6 7 8
# 1 2 3 4

# matrix = [input().split() for _ in range(int(input()))]
# [print(*r) for r in matrix[::-1]]

# Ходы коня
# На шахматной доске 8 \times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.
#
# Формат входных данных
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 11 до 88, снизу вверх)).
#
# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

# Sample Input 1:
#
# b6
# Sample Output 1:
#
# * . * . . . . .
# . . . * . . . .
# . N . . . . . .
# . . . * . . . .
# * . * . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
#
# coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#
# horse= input()
# # print(coor_j.get(horse[0]))
# # print(coor_i.get(horse[1]))
# n = 8
# mtr = [['.' for i in range(8)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if j == coor_j.get(horse[0]) and i == coor_i.get(horse[1]):
#            mtr[i][j] = "N"
#         if (i - coor_i.get(horse[1])) ** 2 + (j - coor_j.get(horse[0])) ** 2 == 5:
#            mtr[i][j] = "*"
#         elif j != coor_j.get(horse[0]) and i != coor_i.get(horse[1]) and (i - coor_i.get(horse[1])) ** 2 + (j - coor_j.get(horse[0])) ** 2 != 5:
#            mtr[i][j] = "."

# 78u789n, m = map(int, input().split())
# for i in range(n):
#     row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
#     print(*row)
#
# Побочная диагональ
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:
#
# числа на побочной диагонали равны 11;
# числа, стоящие выше этой диагонали, равны 00;
# числа, стоящие ниже этой диагонали, равны 22.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
#
# Формат входных данных
# На вход программе подается натуральное число nn — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.
#
# Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.
#
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
# 1 2 2 2
#
# n = int(input())
# matrix =[['0' for i in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if j == n - i -1:
#             matrix[i][j] = 1
#         if j > n - i -1:
#             matrix[i][j] = 2
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
#
#
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.
#
# Формат входных данных
# На вход программе подается натуральное число nn — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
#
# Sample Input 1:
#
# 5
# Sample Output 1:
#
# 1  0  0  0  1
# 0  1  0  1  0
# 0  0  1  0  0
# 0  1  0  1  0
# 1  0  0  0  1
#
# n = int(input())
# matrix =[['0'for i in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==j or j == n - i -1:
#             matrix[i][j] = 1
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
#
# Одинаковые цифры
# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
#
# Формат входных данных
# На вход программе подаются два натуральных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.
#
# Sample Input 1:
#
# 114
# 223
# Sample Output 1:
#
# NO
#
# print(["YES", "NO"][set((input())).isdisjoint(set((input())))])
#
# Даны по 1010-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
#
# Sample Input 1:
#
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 9 8 7 0 9 0 9 8 10
# Sample Output 1:
#
# 10 9 8 0
#
# s1= set(input().split())
# s2= set(input().split())
# s3= set(input().split())
# set1 = set()
# for i in (s3 - s2 -s1):
#     set1.add(int(i))
# print(*(reversed(sorted(set1))))
#
# Даны по 1010-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
#
# Sample Input 1:
#
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 8 8 7 0 6 0 3 8 1
# Sample Output 1:
#
# 9 10
#
# s1= set(map(int, input().split()))
# s2= set(map(int, input().split()))
# s3= set(map(int, input().split()))
# s4 = {0,1,2,3,4,5,6,7,8,9,10}
# set1 = set()
# for i in (s4 - s1 - s3 - s2):
#     set1.add(int(i))
# print(*(sorted(set1)))
#
# Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные значения списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
#
# Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.
#
# Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:
#
# print(*sorted(myset))
#
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# item =  {int(c) for c in items}
# print(*sorted(item))
#
# Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence. Результат вывести на одной строке, в отсортированном по возрастанию виде, разделяя элементы одним символом пробела.
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# print(*sorted({word.strip("(),.:;").lower() for word in sentence.split()}))
#
#
# Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence длиною меньше 44 символов. Результат вывести на одной строке, в отсортированном по возрастанию виде, разделяя элементы одним символом пробела.
#
# Примечание. Учтите, что знаки пунктуации не относятся к словам.
#
# import re
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# words = re.sub(r'[.,;:-?-!)(]', '', sentence)
# # print(words)
# digits = {d for d in words.lower().split() if len(d) < 4}
# print(*(sorted(digits)))
#
# Даны по 1010-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок, которые есть и у первого и второго учеников, но которых нет у третьего ученика.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
#
# Sample Input 1:
#
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 9 8 7 0 9 0 9 8 10
# Sample Output 1:
#
# 5 3 2
#
# set1 = set()
# for i in (set(input().split()) & set(input().split())) - set(input().split()):
#     set1.add(int(i))
# print(*reversed(sorted(set1)))
#
# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести множество чисел, встречающихся только в первой строке.
#
# Sample Input 1:
#
# 1 2 3 4
# 5 6 7 8
# Sample Output 1:
#
# 1 2 3 4
#
#
# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set1 - set2
# l= []
# for i in set3:
#     i = int(i)
#     l.append(i)
# print(*(sorted(l)))
#
# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
#
# Формат входных данных
# На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк с словами.
#
# Формат выходных данных
# Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.
#
# Sample Input 1:
#
# 5
# aAa
# bB
# ccc
# dDdd
# ppppP
# Sample Output 1:
#
# 5
#
# n = int(input())
# all_set = set()
# for i in range(n):
#     set_a = set(input().lower())
#     all_set = all_set.union(set_a)
# print(len(all_set))









