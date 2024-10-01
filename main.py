# if 7:
#     print('phyton thinks its a true')
# else:
#     print('phyton thinks i know nothing')
#
# print('pradedu rink zaliu staskiukus')
import pathlib
import random
import re
from itertools import count
from traceback import print_list

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

# failo_kelias = str(input("Iveskite failo kelia: "))
# if failo_kelias.endswith(".py"):
#     print("Tai yra Python failas")
# else:
#     print("Tai nėra Python failas")

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

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if number1 - number2  ==0:
#     print('pirmi 2 skaiciai yra lygus')
# elif number1 - number3  ==0:
#     print('pirmas ir trecias skaiciai lygus')
# elif number3 > number1:
#     print('trecias yra didesnis uz pirma')
# elif number3 < number1:
#     print('trecias yra mazesnis uz pirma')
# elif number3 * 2 == number2:
#     print('trecias yra didesnis uz pirma')
# else:
#     print("message of dissapointment")

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if (number1 > number2) and (number1 > number3):
#     print('number1 yra didziausias')
# elif (number2 > number1) and (number2 > number3):
#     print('number2 yra yra didziausias')
# elif (number3 > number1) and (number3 > number2):
#     print('number3 yra yra didziausias')

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if (number1 < number2) and (number1 < number3):
#     print('number1 yra maziausias')
# elif (number2 < number1) and (number2 < number3):
#     print('number2 yra yra maziausias')
# elif (number3 < number1) and (number3 < number2):
#     print('number3 yra yra maziausias')

# print('ispausdinkite egzaminu rezultatus')
# rez1 = int(input())
# rez2 = int(input())
# rez3 = int(input())
# vidurkis = (rez1 + rez2 + rez3) / 3
# print(vidurkis)
# if (vidurkis > 8) and (vidurkis < 10):
#     print('vidurkis 8-10')
# elif (vidurkis > 5) and (vidurkis < 8):
#     print('vidurkis 5-8')
# elif (vidurkis < 5):
#     print('vidurkis < 5')

# print('prasau parasykite 2 skaicius')
# number1 = int(input())
# number2 = int(input())
#
# if (number1 > number2) and (number1 == 0):
#     print('number1 yra didesnis uz number2 arba =0')
# if (number2 > number1) and (number2 == 5):
#     print('number2 yra ura didesnis uz number1 arba =5')
# if (number1 > number2) and (number1 == 20):
#     print('number1 yra =20')
# if (number2 > number1) and (number1 < 100):
#     print('number2 yra >100')
# else:
#     print("message of dissapointment")


# print('prasau parasykite savo varda')
# name = (input())
# print('prasau parasykite savo pavarde')
# surname = (input())
# print('prasau parasykite savo gimimo metus')
# birthYear = int(input())
# age = 2024 - birthYear
#
# print(f' "As esu {name} {surname}. Man yra {age} metai(u)." ')



# random_num1 = random.randint(0,4)
# random_num2 = random.randint(0,4)
# random_num1 = 3
# random_num2 = 3
# print(random_num1)
# print(random_num2)
# if random_num1 > 0  and random_num2 > 0 and random_num1 > random_num2 and random_num1 != random_num2:
#     print( round(random_num1 / random_num2, 2))
# elif random_num1 > 0 and random_num2 > 0  and random_num1 < random_num2 and random_num1 != random_num2:
#     print( round(random_num2 / random_num1, 2))
# else:
#     print ('dalyba negalima')





# num1 = random.randint(0, 4)
# num2 = random.randint(0, 4)
# num1 = 4
# num2 = 3
# print(num1)
# print(num2)
# if num1 > num2:
#     print(num1 / num2)
# if num2 > num1:
#     print(num2 / num1)
# if num1 > 0 and num2 > 0:
#     print(num2 / num1)
# if num1 == 0 or num2 == 0:
#     print('nulis')
# else:
#     print('nesamone')


# num1 = random.randint(0, 25)
# num2 = random.randint(0, 25)
# num3 = random.randint(0, 25)
# print(num1)
# print(num2)
# print(num3)
# if num1 != num2 and num1 != num3 and num2 != num3:
#     if num1 > num2 and num1 < num3:
#         print(num1)
#     elif num2 > num1 and num2 < num3:
#         print(num2)
#     elif num3 > num1 and num3 < num2:
#         print(num3)
# else:
#     print('lygus')


# num1a = random.randint(0, 10)
# num2b = random.randint(0, 10)
# num3c = random.randint(0, 10)
# print(num1a)
# print(num2b)
# print(num3c)
# if num1a > num3c and num2b > num3c:
#     print('trikampisC')
# elif num1a > num2b and num3c > num2b:
#     print('trikampisB')
# elif num2b > num1a and num3c > num1a:
#     print('trikampisA')
# if (num1a > num3c and num2b > num3c) or (num1a > num2b and num3c > num2b) or (num2b > num1a and num3c > num1a):
#     print('trikampis')
# else:
#     print('klaida')

#
# num1 = random.randint(0, 2)
# num2 = random.randint(0, 2)
# num3 = random.randint(0, 2)
# num4 = random.randint(0, 2)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# countZeros = 0
# countOnes = 0
# countTwos = 0
#
# if num1 == 0:
#     print("as esu num1 ir esu lygus nuliui")
#     countZeros += 1
# if num2 == 0:
#     print("as esu num2 ir esu lygus nuliui")
#     countZeros += 1
# if num3 == 0:
#     print("as esu num3 ir esu lygus nuliui")
#     countZeros += 1
# if num3 == 0:
#     print("as esu num4 ir esu lygus nuliui")
#     countZeros += 1
#     print("nuliu radau " + str(countZeros))
#
# if num1 == 1:
#     print("as esu num1 ir esu lygus vienetui")
#     countOnes += 1
# if num2 == 1:
#     print("as esu num2 ir esu lygus vienetui")
#     countOnes += 1
# if num3 == 1:
#     print("as esu num3 ir esu lygus vienetui")
#     countOnes += 1
# if num3 == 1:
#     print("as esu num4 ir esu lygus vienetui")
#     countOnes += 1
#     print("vienetu radau " + str(countOnes))
#
# if num1 == 2:
#     print("as esu num1 ir esu lygus dvejetui")
#     countTwos += 1
# if num2 == 2:
#     print("as esu num2 ir esu lygus dvejetui")
#     countTwos += 1
# if num3 == 2:
#     print("as esu num3 ir esu lygus dvejetui")
#     countTwos += 1
# if num3 == 2:
#     print("as esu num4 ir esu lygus dvejetui")
#     countTwos += 1
# print("dvejetu radau " + str(countTwos))



#
# num1 = random.randint(-10, 10)
# num2 = random.randint(-10, 10)
# num3 = random.randint(-10, 10)
# print(num1)
# print(num2)
# print(num3)
#
#
# if num1 > 0:
#     print('[' + str(num1) + ']')
# if num1 == 0:
#     print('(' + str(num1) + ')')
# if num1 < 0:
#     print('{' + str(num1) + '}')
#
# if num2 > 0:
#     print('[' + str(num2) + ']')
# if num2 == 0:
#     print('(' + str(num2) + ')')
# if num2 < 0:
#     print('{' + str(num2) + '}')
#
# if num3 > 0:
#     print('[' + str(num3) + ']')
# if num3 == 0:
#     print('(' + str(num2) + ')')
# if num3 < 0:
#     print('{' + str(num3) + '}')


# print("parafino namai")
# ZvakiuSkaicius = random.randint(5, 3000)
# ZvakiuSkaicius = 2114
# print(ZvakiuSkaicius)
# kaina = 1
# if ZvakiuSkaicius < 1000:
#     print(ZvakiuSkaicius  * kaina)
# # if ZvakiuSkaicius >= 1000 and ZvakiuSkaicius < 2000:
# if 1000 < ZvakiuSkaicius < 2000:
#     print(ZvakiuSkaicius * kaina * 0.97)
# if ZvakiuSkaicius > 2000:
#     print(ZvakiuSkaicius * kaina * 0.96)

# num1 = random.randint(0, 100)
# num2 = random.randint(0, 100)
# num3 = random.randint(0, 100)
# print(num1)
# print(num2)
# print(num3)
#
# print(round((num1 + num2 + num3)/3))
#
# if num1 < 10:
#     print((num2 + num3) / 2)
# if num1 > 90:
#     print((num2 + num3)/2)
# if num2 < 10:
#     print((num1 + num3) / 2)
# if num2 > 90:
#     print((num1 + num3)/2)
# if num3 < 10:
#     print((num1 + num2) / 2)
# if num3 > 90:
#     print((num1 + num2)/2)


# name = 'Kevin'
# surname = 'Costner'
# if len(name) > len(surname):
#     print(surname)
# else:
#     print(name)

# print(str.upper(name), str.lower(surname))

# print(str.upper(name[0]) + str.upper(surname[0]))
# print(str.upper(name[2]) + str.upper(surname[2]))
# print(str.upper(name[3]) + str.upper(surname[3]))


# fraze ='An American in Paris'
# # updateFraze = fraze.replace('a' or 'A', '*') #lawer pasikeicia#
# updateFraze = fraze.replace('a' and 'A', '*') #upper pasikeicia#
# print(updateFraze)
#
# updateFraze = {"a": "*", "A": "*"}
# print(updateFraze)

# fraze = 'An American in Paris'
# updateFraze = fraze.replace("a", "").replace("A", "")
# print(updateFraze)

# fraze = 'An American in Paris'
# replaced = re.sub('[aA]', '*', fraze)
# print(replaced)


# fraze ='An American in Paris'
# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
# result  = ''
#
# print("\n After removing Vowels:", result)

# phrase = 'An American in Paris'
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# phrase = "Breakfast at Tiffany's"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)


# phrase = "2001: A Space Odyssey"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# phrase = "It's a Wonderful Life"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# print('labas rytas')
# labas= input()
# print('kuri siandien diena?')
# diena= input()
# print('ar isgerei vitaminus?')
# vitaminai= input()
# if vitaminai == 'taip':
#     print('grazios dienos Princess')
# if vitaminai == 'ne':
#     print('mars isgerti vitaminu')


# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# regex2 = re.findall("Star Wars: Episode", starWars)
# print(regex2)
#
# epizodas = re.sub("Star Wars: Episode", "",  starWars)
# print(epizodas)
# epizodo_nr  = re.sub("- A New Hope", "", epizodas)
# print(epizodo_nr)
# epizodo_numeris = re.sub("Star Wars: Episode  | - A New Hope", "", starWars)
# print(epizodo_nr)

# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# print(starWars[-14:-13])
# print(re.sub(r'\D+', '', starWars ))

# Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.

# vardai = ['Asta', 'Naglis', 'Regimantas', 'Augustinas', 'Teresa', 'Darius', 'Arina', 'Gintaras', 'Monika', 'Alina',]
# # print(vardai [0])
# # print(vardai [5])
# print('pirmas vardas sarase:', vardai [0])
# print('nariu skaicius:', len(vardai))
# print('paskutinis vardas sarase:',  vardai[len(vardai)-1])

# Susikurkite list žmonių ūgiams saugoti ir užpildykite jį informacija.
# Išveskite viso šio list duomenis bei kiek ūgių turite.

# ugis = [169, 170, 215, 198, 154, 210, 214]
#
# print('ugiu sarasas:', ugis)
# print('ugis:', len(ugis))
# print('ugiu skaicius:',  len(ugis))

# Susikurkite list pažymiams saugoti. Pamėginkite sukurti programą, kur
# vartotojas galėtų suvesti norimą kiekį naujų duomenų. Galiausiai išveskite
# visus pažymius ir jų kiekį.

# pazimys = [10,7,9,8,9,8,8]
# print(pazimys)
# print('pazymiu skaicius:',  len(pazimys))
# suma = pazimys[0] + pazimys[1] +pazimys[2] +pazimys[3] +pazimys[4] +pazimys[5] +pazimys[6]
# print (suma)
# vidurkis = suma / len(pazimys)
# print('pazymiu vidurkis:', vidurkis)
# print('pazimiu vidurkis:', round(vidurkis, 2))

# Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list,
# tiek papildytą duomenimis. Pamėginkite papildyti programą, kad
# vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.

# city = ['Alytus', 'Klaipeda','Vilnius','Telsiai','Raseiniai','Kaunas']
# print(city)
# city.append('Marijampole')
# city.append('Zarasai')
# print(city)
# city.insert(1, 'Marijampole')
# print(city)

# Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# apygarda.pop()
# print(apygarda)
# apygarda.pop(0)
# apygarda.pop(5)
# print(apygarda)

# Sukurkite list su pasirinktais duomenimis. Patikrinkite ar sąraše yra
# daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# apygarda.pop(5)
# print(apygarda)
# apygarda.clear()
# print(apygarda)

# Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. Leiskite vartotojui
# atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa
# pasakytų ar tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# print('Alytus' in apygarda)
# print(apygarda.index('Dubiciu'))

# Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. Galite
# padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas.
# Programa turi pasakyti kiek dešimtukų studentas turi.
# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
# print(studentuPazymiai)
# # print(studentuPazymiai.index(10))
# print(studentuPazymiai.index(10,0,10))
# print(studentuPazymiai.count(10))

# Susikurkite automobilių markių sąrašą ir užpildykite jį duomenimis
# (kuriantis sąrašą arba su vartotojo įvestimi). Išveskite turimus duomenis
# ekrane.
# Tuomet surikiuokite automobilių markes didėjimo tvarka ir
# išveskite.
# Taip pat, surikiuokite mažėjimo tvarka ir išveskite.

# marke = ['BMW', 'Opel', 'Volo','Audi', 'Porshe', 'Mercedes', 'Volswagen']
# # print(marke)
# # print(len(marke))
# # marke.sort()
# # print(marke)
# # marke.reverse()
# # print(marke)

# Susikurkite studento pažymių sąrašą ir užpildykite duomenimis. Išveskite
# tris didžiausius turimus pažymius.


# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
# print(studentuPazymiai)
# studentuPazymiai.sort()
# print(studentuPazymiai)
# studentuPazymiai.reverse()
# print(studentuPazymiai)
# print(studentuPazymiai [:3])

# Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. Jeigu
# studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių
# pažymių jis turi.

# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
#
# print(studentuPazymiai.count(1) + studentuPazymiai.count(2) + studentuPazymiai.count(3) + studentuPazymiai.count(4))

# Susikurkite pasirinktą sąrašą su duomenimis. Pritaikykite list slicing tokiais
# būdais ir gautus atsakymus išveskite:
# 1. Paimkite pirmus tris narius.
# 2. Paimkite du narius, pradedant trečiu.
# 3. Paimkite paskutinius keturis narius.
# 4. Paimkite kas antrą narį, pradedant trečiu nariu.
# 5. Paimkite visus atbuline tvarka.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# print(apygarda [:3])
# print(apygarda [3:5])
# print(apygarda [4:])
# print(apygarda [3::2])
# apygarda.reverse()
# print(apygarda)

# Susikurkite list studentų vidurkiams saugoti. Išsitraukite ir pasidėkite į
# atskirą list tris didžiausius pažymius (galite surikiuoti ir išsikirpti ką reikia).

# vidurkis = [4.5, 6.7, 8, 10, 6.9, 8.9]
# print(vidurkis)
# vidurkis.sort()
# print(vidurkis)
# vidurkis.reverse()
# print(vidurkis)
# print(vidurkis [:3])

# Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas,
# įvesdamas visus norimus žodžius. Po kiekvieno įvedimo jam turėtų būti
# parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį
# surikiuokite iš naujo.
# auksoZodziai = ['Alaninas', 'Kabala','Piala', 'Marsala', 'Kupala']
# print(auksoZodziai)
#
#
# kopija = auksoZodziai[:]
# print(kopija)
# auksoZodziai[0] = 'naujas'
# print(auksoZodziai)
# print(kopija)

# Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai). - NEPADARYTA

# Su for pagalba penkis kartus išveskite savo vardą.
# for sk in range(5):
#     print('Evita')

# Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.
# for sk in range(11):
#     print('Evita' + str(sk))

# Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15.

# for sk in range(0, 16,2):
#     print('Evita' + str(sk))

# Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...

# for sk in range(1, 20,3):
#     print('Evita' + str([sk]))

# Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.

for sk in range(1, 20):
    if sk % 4 ==0:
        print('dalinasi is 4' + '-' + str(sk))
    else:
        print('nesidalinas')