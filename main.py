# if 7:
#     print('phyton thinks its a true')
# else:
#     print('phyton thinks i know nothing')
#
# print('pradedu rink zaliu staskiukus')
import pathlib

# print('hello')
# print("hello 9/24")

#
# print('prasau parasykite savo varda')
# name = input()
# print('koks Jusu amzius')
# age = int(input())
# if age < 18:
#     print(name + ', jus per jaunas')
# if age >= 18:
#     print(name + ' Jus galite balsuoti')

# print('prasau parasykite 4 skaicius')
# skai1 = int(input())
# skai2 = int(input())
# skai3 = int(input())
# skai4 = int(input())
# vidurkis = (skai1 + skai2 + skai3 + skai4) / 4
# print(vidurkis)
# if vidurkis >=5:
#     print('vidurkis teigiamas')
# if vidurkis <5:
#     print('vidurkis neigiamas')

# print('prasau parasykite skaiciu')
# number = int(input())
# isItGood = False
# if number % 5 ==0:
#     print(number * 1, '\n', number * 2, '\n', number * 3, '\n', number * 4, '\n', number * 5 )
#     isItGood = True
# if number % 2 ==0:
#     print(number,'\n', number * number, '\n', number / 2)
#     isItGood = True
# if number % 7 != 0:
#     print('prasau parasykite kita skaiciu')
#     number2 = int(input())
#     print( number2 + number2, '\n', number2 - number2, '\n', number2 * number2, '\n', number2 / number2)
#     isItGood = True
# if not isItGood:
#     print("message of dissapointment")
#
#
# if number % 5 ==0:
#     print(number * 1, '\n', number * 2, '\n', number * 3, '\n', number * 4, '\n', number * 5 )
# elif number % 2 ==0:
#     print(number,'\n', number * number, '\n', number / 2)
# elif number % 7 != 0:
#     print('prasau parasykite kita skaiciu')
#     number2 = int(input())
#     print( number2 + number2, '\n', number2 - number2, '\n', number2 * number2, '\n', number2 / number2)
# else:
#     print("message of dissapointment")

# file_format = pathlib.Path('main.py').suffix
# if file_format == '.py':
#     print('failas . py')
# else:
#     print('failas ne .py')

# print('prasau parasykite skaiciu')
# number = int(input())
# if number % 2 ==0:
#     print('kintamasis yra lyginis')
# elif number % 5 ==0:
#     print('kintamasis dalijasi is 5')
# elif number ==3:
#     print('kintamasis yra 3')
# else:
#     print("message of dissapointment")

print('prasau parasykite 3 skaicius')
number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 - number2  ==0:
    print('pirmi 2 skaiciai yra lygus')
elif number1 - number3  ==0:
    print('pirmas ir trecias skaiciai lygus')
elif number3 > number1:
    print('trecias yra didesnis uz pirma')
elif number3 < number1:
    print('trecias yra mazesnis uz pirma')
elif number3 * 2 == number2:
    print('trecias yra didesnis uz pirma')
else:
    print("message of dissapointment")