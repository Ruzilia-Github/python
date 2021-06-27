# Символы в диапазоне
# На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения в диапазоне от aa до bb (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
#
# Формат входных данных
# На вход программе подается два натуральных числа, каждое на отдельное строке.
#
# Формат выходных данных
# Программа должна вывести текст в соотвествии с условием задачи.
#
# Sample Input 1:
#
# 65
# 70
# Sample Output 1:
#
# A B C D E F
#
# a = int(input())
# b = int(input())
# for i in range(a,b + 1):
#     print(chr(i), end=' ')

# Простой шифр
# На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.
#
# Sample Input:
#
# Hello world!
# Sample Output:
#
# 72 101 108 108 111 32 119 111 114 108 100 33

# a = input()
# for i in a:
#     print(ord(i), end=' ')
#
# Шифр Цезаря 🌶️
# Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.
#
# Формат входных данных
# В первой строке дается число n \, (1 \le n \le 25)n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.
#
# Формат выходных данных
# Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение, а не закодировать.
#
# Sample Input 1:
#
# 1
# bwfusvfupdbftbs
# Sample Output 1:
#
# avetruetocaesar

# Ввести шаг сдвига.
# Ввести строку.
# Цикл на длину строки.
#     Находим n:
#     n = ord(строка[i]) - шаг сдвига
#     Проверяем условие n < 97:
#         n = 122 - (96 - n)
#     Печатаем(не забудь про chr и end )



# n =  1   #int(input())
# b= "bwfusvfupdbftbs"  #input()
# a = 0
# for i in b:
#     # print(i, end='')
#     a = ord(i) + n
#     # print(n, end='')
#     if a < 97:
#         a = a + 26
#     else:
#         a = a - 26
#     print(chr(a), end='')


# Список букв
# На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
#
# Формат входных данных
# На вход программе подается натуральное число n, \, n \le 26n,n≤26.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input 1:
#
# 1
# Sample Output 1:
#
# ['a']
# number=[]
# n = int(input())
# for i in range(n):
#     number.append((chr(i + 97)))
# print(number)

# Все сразу 1
# Дополните приведенный код, чтобы он:
#
# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# Вывел список с удаленным первым и последним элементами.
# Примечание. Каждый вывод осуществлять с новой строки.
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))# Вывел длину списка;
# print(numbers[-1])# Вывел последний элемент списка;
# print(numbers[::-1])# Вывел список в обратном порядке (вспоминаем срезы);
# if 5 and 17 in numbers:
#     print("YES")
# else:
#      print("NO")# Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# print(numbers[1:-1]) # Вывел список с удаленным первым и последним элементами.

# Список строк
# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает из указанных строк список и выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из указанных строк.
#
# Sample Input:
#
# 5
# C#
# C++
# C
# Python
# F#
# Sample Output:
#
# ['C#', 'C++', 'C', 'Python', 'F#']

# n = int(input())
# l = []
# for i  in range(n):
#     a = input()
#     l.append(a)
# print(l)
#
# Алфавит
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z.

# l = []
# for i in range(1, 27):
#     l.append(chr(i+96) * i)
# print(l, end='')

# Список кубов
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из кубов указанных чисел.
#
# Sample Input 1:
#
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
#
# [1, 8, 27, 64, 125]

# n = int(input())
# l = []
# for i  in range(n):
#     a = int(input())
#     l.append(a**3)
# print(l)
#
# Список делителей
# На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.
#
# Формат входных данных
# На вход программе подается натуральное число nn.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.
#
# Sample Input 1:
#
# 17
# Sample Output 1:
#
# [1, 17]

# n = int(input())
# l = []
# for i in range(1,n + 1):
#     if n % i == 0:
#         l.append(i)
# print(l)
#
# Суммы двух
# На вход программе подается натуральное число n \ge 2n≥2, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.
#
# Sample Input 1:
#
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
#
# [3, 5, 7, 9]

# n = int(input())
# a = 0
# b = 0
# l = []
# for i in range(n):
#     number = int(input())
#     b = a
#     a = number
#     if i >= 1:
#         l.append(a+b)
# print(l)
#
# Удалите нечетные индексы
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список в соответствии с условием задачи.
#
# Примечание. Используйте оператор del.
#
# Sample Input 1:
#
# 10
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Sample Output 1:
#
# [0, 2, 4, 6, 8]

# n = int(input())
# l = []
# for i in range(n):
#     number = int(input())
#     l.append(number)
# del l[1::2]
# print(l)
#
#
# n = int(input())
# l = []
# for i in range(n):
#     number = int(input())
#     if i % 2 == 0:
#        l.append(number)
# print(l)


# k-ая буква слова 🌶️🌶️
# На вход программе подается натуральное число nn и nn строк, а затем число kk. Напишите программу, которая выводит kk-ую букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число nn,  далее nn строк, каждая на отдельной строке. В конце вводится натуральное число kk – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.
# Sample Input:
#
# 5
# abcdef
# bcdefg
# cdefgh
# defghi
# efghij
# 2
# Sample Output:
#
# bcdef

# number1 = int(input())
# l=[]
#
# for i in range(number1):
#     a = input()
#     l.append(a)
# number2 = int(input())
# last=[]
#
# for j in l:
#     if len(j) < number2:
#         continue
#     else:
#         print(j[(number2)-1], end="")


# Символы всех строк
# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из символов всех введенных строк.
#
# Примечание. В результирующем списке могут содержаться одинаковые символы.
#
# Sample Input:
#
# 3
# abc
# def
# ghi
# Sample Output:
#
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# n = int(input())
# l = []
# for i in range(n):
#     l.extend(input())
# print(l)


# numbers = [0, 4, 5, 6, 7, 8, 9, 10]
#
# for num in numbers:
#     print(num, end=' ')
#
# numbers = [0, 4, 5, 6, 7, 8, 9, 10]
#
# for num in range(len(numbers)):
#     print(num, end=' ')

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
#


# Значение функции
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x) = x^2 + 2x + 1f(x)=x
# 2
#  +2x+1, каждое на отдельной строке.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
#
# Примечание. Для первого теста имеем:
# f(1) = 1^2 + 2\cdot 1 + 1 = 4, \, f(2) = 2^2 + 2\cdot 2 + 1 = 9, \, f(3) = 3^2 + 2 \cdot 3 + 1 = 16, \ldots
# f(1)=1
# 2
#  +2⋅1+1=4,f(2)=2
# 2
#  +2⋅2+1=9,f(3)=3
# 2
#  +2⋅3+1=16,…

# n = int(input())
# l = []
# for i in range(n):
#     a = int(input())
#     l.append(a)
#     print(a)
# print()
# for j in l:
#     print(j ** 2 + 2 * j + 1)

# Remove outliers
# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
#
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input:
#
# 10
# 9
# 17
# 189
# 3
# 55
# 78
# 11
# 7
# 888
# 160
# Sample Output:
#
# 9
# 17
# 189
# 55
# 78
# 11
# 7
# 160

# n = int(input())
# l = []
# min_n = 0
# max_n = 0
# for i in range(n):
#     a = int(input())
#     l.append(a)
# l.remove(min(l))
# del l[l.index(max(l))]
# # l.remove(max(l))
# print(*l, sep='\n')
#
# Без дубликатов
# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Считайте, что все строки состоят из строчных символов.
#
# Sample Input:
#
# 5
# first
# second
# first
# third
# second
# Sample Output:
#
# first
# second
# third

# n = int(input())
# l = []
# for i in range(n):
#     a = input()
#     if a in l:
#         continue
#     else:
#         l.append(a)
# print(*l, sep="\n")
#
# Google search - 1
# На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
#
# Формат входных данных
# На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем один поисковый запрос.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.
#
# Sample Input:
#
# 5
# Язык Python прекрасен
# C# - отличный язык программирования
# Stepik - отличная платформа
# BEEGEEK FOREVER!
# язык Python появился 20 февраля 1991
# язык
# Sample Output:
#
# Язык Python прекрасен
# C# - отличный язык программирования
# язык Python появился 20 февраля 1991

# n = int(input())
# l = []
# for i in range(n):
#     a = input()
#     l.append(a)
# b = input()
# for j in l:
#     if b.lower() in j.lower():
#         print(j)
#
# Google search - 2 🌶️🌶️
# На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
#
# Формат входных данных
# На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем число kk, затем сами поисковые запросы.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.
#
# Sample Input:
#
# 5
# Язык Python прекрасен
# C# - отличный язык программирования
# Stepik - отличная платформа
# BEEGEEK FOREVER!
# язык Python появился 20 февраля 1991
# 2
# язык
# python
# Sample Output:
#
# Язык Python прекрасен
# язык Python появился 20 февраля 1991

# n = int(input())
# l = []
# l2 = []
# l3 =[]
# for i in range(n):
#     a = input()
#     l.append(a)
# n2 = int(input())
# for j in range(n2):
#      b = input()
#      l2.append(b)
# for i in l:
#     count = 0
#     for j in l2:
#         if j.lower() in i.lower():
#               count +=1
#     if count == n2:
#         print(i)
#
#
# l1 = [input() for _ in range(int(input()))]
# l2 = [input() for _ in range(int(input()))]
#
# for i in l1:
#     c = 0
#     for j in l2:
#         if j.lower() in i.lower():
#             c += 1
#         if c == len(l2):
#             print(i)


# Negatives, Zeros and Positives
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input 1:
#
# 7
# 3
# -4
# 1
# 0
# -1
# 0
# -2
# Sample Output 1:
#
# -4
# -1
# -2
# 0
# 0
# 3
# 1


# l = [int(input()) for _ in range(int(input()))]
# negative = []
# positive = []
# zero = []
# for i in l:
#     if i < 0:
#         negative.append(i)
#     elif i == 0:
#         zero.append(i)
#     else:
#         positive.append(i)
# print(*negative, sep = '\n')
# print(*zero, sep = '\n')
# print(*positive, sep = '\n')
#
#
#
#
# n = [int(input()) for _ in range(int(input()))]
# [print(i) for i in n if i < 0]
# [print(i) for i in n if i == 0]
# [print(i) for i in n if i > 0]

# Построчный вывод
# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input:
#
# У лукоморья дуб зеленый златая цепь на дубе том
# Sample Output:
#
# У
# лукоморья
# дуб
# зеленый
# златая
# цепь
# на
# дубе

# s = input().split()
# for i in s:
#     print(i)
# Инициалы
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input:
#
# Владимир Семенович Высоцкий
# Sample Output:
#
# В.С.В.

# s = input().split()
# a = []
# for i in s:
#     a.append(i[0])
# print(*a, sep='.', end='.')
#
# Windows OS
# В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
#
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу, которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input:
#
# C:\Windows\System32\calc.exe
# Sample Output:
#
# C:
# Windows
# System32
# calc.exe


# s = input()
# print(*s.split('\\'), sep = "\n")
#
# Диаграмма
# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.
#
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# +
# ++
# +++
# ++++
# +++++

# s = input().split()
# for i in s:
#     print("+" * int(i))
#
#
# Корректный ip-адрес
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
#
# Формат выходных данных
# Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
#
# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
#
# Sample Input 1:
#
# 192.168.0.3
# Sample Output 1:
#
# ДА

# s =input().split('.')
# count = 0
# for i in s:
#     if 0 <= int(i) <= 255:
#           count +=1
# if count == 4:
#     print("ДА")
# else:
#     print("НЕТ")
#
# Добавь разделитель
# На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.
#
# Формат входных данных
# На вход программе подается строка текста и строка разделитель, каждая на отдельной строке
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Sample Input 1:
#
# 1234567
# *
# Sample Output 1:
#
# 1*2*3*4*5*6*7

# a = list(input())
# # b = input()
# # print(b.join(a))
#
# Количество совпадающих пар
# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести одно число – количество пар элементов, равных друг другу.
#
# Sample Input 1:
#
# 1 7 5 7 5
# Sample Output 1:
#
# 2

# s = input().split()
# count = 0
# # for i in s:
# #     for j in s:
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if int(s[i]) == int(s[j]):
#             count +=1
# print(count)

# numbers = [8, 9, 10, 11]
#
# numbers.remove(9)
# numbers.insert(1, 17) # Заменил второй элемент списка на 17;
# numbers.insert(4, 4) # Добавил числа 4, 5 и 6 в конец списка;
# numbers.insert(5, 5)
# numbers.insert(6, 6)
# numbers.remove(8)# Удалил первый элемент списка;
# numbers = numbers*2 # Удвоил список;
# numbers.insert(3, 25) # Вставил число 25 по индексу 3;
# print(numbers) # Вывел список, с помощью функции print().
#
# numbers = [8, 9, 10, 11]
#
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)
#
# Mikhail Oloventsev
# 4 месяца назад
# Ссылка
#
# .
#
#
# Решение #363739110
# 9 февраля 2021 г., 09:46
# l = [8, 9, 10, 11]
# l[1] = 17
# l += [4, 5, 6]
# del l[0]
# l *= 2
# l.insert(3, 25)
# print(l)


# Середина отрезка
# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка (x_1; \, y_1)(x
#
#  ) и возвращает координаты точки являющейся серединой данного отрезка.
#
# Примечание 1. Координаты середины отрезка вычисляются по формуле:
# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     a = (x1 + x2) / 2
#     b = (y1 + y2) / 2
#     return a, b
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# Площадь и длина
# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
#
# Примечание 1. Длина окружности и площадь круга радиуса rr вычисляются по формулам:
#
# С = 2 \pi r, \, \, \, S = \pi r^2.
# С=2πr,S=πr
# 2
#  .
# Примечание 2. Для числа \piπ используйте глобальную константу из модуля math.
#
# Примечание 3. Следующий программный код:
#
# print(get_circle(1))
# print(get_circle(1.5))
# должен выводить:
#
# 6.283185307179586 3.141592653589793
# 9.42477796076938 7.0685834705770345

# from math import pi
import math
# объявление функции
def get_circle(radius):
    return (2 * (math.pi)) * radius, (math.pi) * (radius ** 2)


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
