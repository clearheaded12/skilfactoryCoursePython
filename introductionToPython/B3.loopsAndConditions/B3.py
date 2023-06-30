# 1. Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7.
# def someDigit(n):
#     # strDigit = list(str(n))
#     # digitList = map(int, strDigit)
#     return '3' in str(n) and '7' in str(n)
#
#
# print(someDigit(13))

# Result = a if a > b else b

# 2. Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
# A = int(input('Enter first num: '))
# B = int(input('Enter second num: '))
# C = int(input('Enter third num: '))
#
# if (A < 45 and B <= 45 and C <= 45) or (A <= 45 and B < 45 and C <= 45) or (A <= 45 and B <= 45 and C < 45):
#     print('There is a number less than 45 and only one')
# else:
#     print('There are no numbers less than 45 or there are several of them')

# 3. Дано двузначное число. Определить: входит ли в него цифра 5.
# Попробуйте решить её с использованием целочисленного деления и деления с остатком.
# n = int(input('Enter number please: '))
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# 4. Записать логические выражения, которые определяют, что число А не принадлежит интервалу

# от -10 до -1 или интервалу от 2 до 15.
# A = int(input('Enter some number '))
#
# if not ((-10 <= A <= -1) or (2 <= A <= 15)):
#     print('The number is not in this range')
# else:
#     print('The number is in this range')

# 5. Проверить, все ли элементы в списке являются уникальными.

# list_ = [-5, 2, 4, 8, 12, -7, -5]
#
# print(len(list_) == len(set(list_)))

# 6. Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).

# num = 112211
# print(str(num) == str(num)[::-1])
