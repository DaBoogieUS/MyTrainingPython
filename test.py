########################################
# 36. MAP, FILTER and Lamda Expressions
########################################

#################
# MAP
#################
# Example 1
def sum_of_two_numbers(x):
    return x+x

number_list = [1, 2, 3, 4, 5, 6, 7]
result = map(sum_of_two_numbers, number_list) #складываем каждое число на него его

# for item in result:
#     print(item)  # 2,4,6,8,10,12,14

print(list(result)) # получаем сумму сразу в список [2,4,6,8,10,12,14]

# MAP
# Example2
def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'was', 'name', 'he']

#в функции MAP функцию нашу мы указываем без (), это важно, иначе ошибка
print(list(map(is_a_in_string, string_list)))
# String has not "a"
# String has "a"
# String has "a"
# String has not "a"
#[False, True, True, False]


#################
# FILTER
#################
# Example 1
##################
def is_number_odd(number):
     return  number % 2 == 1

print(list(filter(is_number_odd, number_list)))  # [1, 3, 5, 7]

print(list(filter(is_a_in_string, string_list)))  # [1, 3, 5, 7]

#################
# Lamda Expressions
#################
# Example 1
#"lambda number: number ** 3"  это по сути функция аналогичная этой функции:
#def cube(number):
#    return number ** 3
print(list(map(lambda number: number ** 3 , number_list)))
#[1, 8, 27, 64, 125, 216, 343]
print(list(filter(lambda number: number % 2 == 1, number_list)))
#[1, 3, 5, 7]
print(list(filter(lambda number: number % 2 == 0, number_list)))
#[2, 4, 6]

print(list(map(lambda string: string[-1], string_list)))
#['i', 's', 'e', 'e']

print(list(map(lambda string: string[::-1], string_list)))
#['ih', 'saw', 'eman', 'eh']


###########################################
# 37. ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕННЫХ (SCOPE) LEGB RULE
###########################################
#nonlocal
#global - не очень хорошая практивка изменять переменные снизу, потом тяжело отлавливать ошибки
print('#37')

pi = 'outer pi variable'

def print_pi():
    pi = 'inner pi variable'
    print(pi)

print_pi()
print(pi)

# Local ScopeW сперва ищется переменная внутри
pi = 'global pi variable'
def inner():
    pi = 'inner pi variable'
    print(pi)

inner()

# Enclosed Scope
pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        nonlocal pi
        print(pi)
    inner()

outer()
print(pi)



###########################################################
#38. Объектно-ориентированное программирование (ООП). Введение
############################################################
print('#38')
class MyFristClass:
    pass
object_of_my_class = MyFristClass()
print(type(object_of_my_class)) # <class '__main__.MyFristClass'>



###########################################################
#39. Атрибуты
############################################################
print('#39')


class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

mazda_car = Car(name='Mazda CX7', color='red', year=2021, is_crashed=True)
print(mazda_car.name)
print(mazda_car.color)
print(mazda_car.year)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)

bmv_car = Car(name='BMV', color='yellow', year=2022, is_crashed=False)
print('\n' + bmv_car.name)
print(bmv_car.color)
print(bmv_car.year)
print(bmv_car.is_crashed)
print(bmv_car.wheels_number)

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)

###########################################################
#40. Методы
############################################################
print('#40')

class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        self.city = city
        print(self.name + ' is driving to ' + self.city)


    def change_color(self, new_color):
        self.color = new_color


opel_car = Car('Opel Tigra', 'black', '2019', True)
mazda_car = Car('Mazda CX7', 'Black', 1987, False)
mazda_car.drive('Chicago')
opel_car.drive('Los Angeles')
opel_car.change_color('Orange')

print(opel_car.wheels_number)
print(opel_car.name)
print(opel_car.year)
print(opel_car.color)
print(opel_car.is_crashed)

####### NEW EXAMPLE
class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius

    def ger_area(self):
        return self.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius

circle_1 = Circle(3)
print(circle_1.ger_area())
#print(circle_1.get_circumference())
print(circle_1.circumference)

###########################################################
#41. Методы класса
############################################################
print('#41')

class Gamer:
    active_gamers = 0

    @classmethod #метод уровня класса
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod #метод уровня класса
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)


    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self. points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')

gamer_1 = Gamer('hell boy', 23, 5, 13)
gamer_2 = Gamer('Poter', 13, 7, 34)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()
print(gamer_2.get_age())
gamer_2.get_adult_level_permission()
print(Gamer.active_gamers)
gamer_1.logout()
print(Gamer.active_gamers)


james = Gamer.gamer_from_string('James, 34, 2, 45')
jane = Gamer.gamer_from_string('Jane, 54, 23, 98')
print(james.get_age())
print(jane.get_level())

print(Gamer.get_active_gamers())

#создание словаря
my_dict = dict.fromkeys((1,2,3), ('apple', 'orange', 'banana'))
print(my_dict)

###########################################################
#42. Наследование (Inherotance). Полиморфизм
############################################################
print('#42')


class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')

    def drive(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('The cargo is loaded. Weight is ' + str(weight) + 'lb.')

man_truck = Truck('Man', 'white', 2015, False)

man_truck.drive('New Yrok') #Man is driving to New Yrok
print(man_truck.wheels_number)
print(man_truck.color)
man_truck.change_color('red')
print(man_truck.color)
man_truck.load_cargo(4000)


#################
# POLYMORPHISM
#################

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Class successor must implement this method')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying meow')

class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying pee-pee-pee')

class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying nothing')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')
freddy = Fish('Freddy')

pet_list = [spike, tom, jerry, freddy]

for pet in pet_list:
    pet.speak()
#Spike is saying woof
#Tom is saying meow
#Jerry is saying pipipi

def pet_voice(pet):
    pet.speak()

pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)
pet_voice(freddy)

print('TASK 42')
# Вопросы к этому заданию 42. Наследование (Inherotance). Полиморфизм
# Создайте класс GameCharacter с атрибутами name, health, level
# и методом speak(), который выводит на печать 'Hi, my name is '
# '(значение атрибута name)'.
#
# Создайте класс Villain, наследник класса GameCharacter с теми же
# атрибутами, методом speak(), который выводит на печать 'Hi, my name '
# is (значение атрибута name) and I will kill you', методом kill(), '
# который принимает в качестве параметра объект класса GameCharacter,
# присваивает атрибуту health этого объекта значение 0 и  выводит на печать
# 'Bang-bang, now you're dead'


class GameCharacter():
    def __init__(self, name, health, level):
        self.name = name
        self. health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)

class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')

    def kill(self, other):
        other.health = 0
        print('Bang-bang, now you\'re dead')

Vasya = GameCharacter('Vasya', 100, 12)
Vasya.speak()
villain_1 = Villain('Killer', 95, 199)

villain_1.speak()
print(Vasya.health)
villain_1.kill(Vasya)
print(Vasya.health)




##########################################
#46. Встроенные модули
##########################################
print('46. Встроенные модули')

#variant #1 импорт всего модуля
import random
x = random.randint(1,10)
print(x)

#variant #2 импорт только функции из модуля
from random import randint
x = randint(1,10)
print(x)

#variant #3 импорт функции подсвоим именем
from random import shuffle as shuffle_my_list
my_list = [1,2,3]
shuffle_my_list(my_list)
print(my_list)

# Вопросы к этому заданию
# Импортируйте встроенный модуль math. Вычислите при помощи функций этого модуля:
# 1. Корень квадратный из числа 123456789
# 2. Факториал числа 987
# 3. 876 в степени 54

import math
x = math.sqrt(123456789)
print(x)

y = math.factorial(987)
print(y)

z = math.pow(876, 54)
print(z)




###################################
#47. Создание своих модулей
#################################
print('47. Создание своих модулей')
from goodbyes import say_goodbye as my_good_bye
import greetings


greetings.say_hello()
greetings.say_hey_there()
greetings.say_hi()

my_good_bye()
my_good_bye()

###################################
#48. Внешние модулей
#################################
print('48. Внешние модулей')

import termcolor

print(termcolor.colored('Hello', 'red', 'on_white'))

###################################
#49. __name__ and '__main__'
#################################
print(termcolor.colored('\n49. __name__ and \'__main__\'', 'red'))

print(1)
print('string')

print(__name__)

def function1():
    print('функция 1')

def function2():
    print('функция 2')

if __name__ == '__main__':
    function1()
    function2()
else:
    print('блаблабла')


###################################
#50. Чтение текстовых файлов
#################################
print(termcolor.colored('\n50. Чтение текстовых файлов', 'red'))

#x = input('Input something')
#print('Output something ' + x)
print(1,2,3, sep=':', end='\n')
print(1,2,3, sep=',', end=' ')
print(1,2,3, sep=';', end='')
print('')
print('')

# loremd = open('ex.txt', 'r')
# for line in loremd:
#     print(line, end='')
# loremd.close()

# loremd = open('ex.txt', 'r')
# for line in loremd:
#     if 'let' in line.lower():
#         print(line, end='')
# loremd.close()

#второй способ открыть файл с помощью with, не нужно закрывать файл после использования
# with open('ex.txt', 'r') as lorem:
#     for line in lorem:
#         if 'mary' in line.lower():
#             print(line, end='')

#еще один вариант, readline() читает одну строку
# with open('ex.txt', 'r') as lorem:
#     line = lorem.readline()
#     while line:
#         print(line, end='')
#         line = lorem.readline()

#еще один вариант, readlines() читает все строки и записываем строки в список
with open('ex.txt', 'r') as lorem:
    lines = lorem.readlines()

for line in lines:
    print(line, end='')

#в случае больших файлов лучше перебирать построчно с помощью readline()


###################################
#51. Запись текстовых файлов
#################################
print(termcolor.colored('\n51. Запись текстовых файлов', 'red'))


# запись в документ из списка
# color_list = ['red', 'yellow', 'indigo', 'black', 'green']
#
# with open('ex_write.txt', 'w') as ex_write:
#     for color in color_list:
#         print(color, file=ex_write)

# чтение документа
color_list = []
with open('ex_write.txt', 'r') as ex_write:
    for color in ex_write:
        color_list.append(color.strip('\n'))

print(color_list)

# добавление одной строки в документ
with open('ex_write.txt', 'a') as ex_write:
    print('dark green', file=ex_write)
    print('dark blue', file=ex_write)



###################################
#52. Двоичная система счисления
#################################
print(termcolor.colored('\n52. Двоичная система счисления', 'red'))


#ДЕСЯТИЧНАЯ СИСТЕМА
x = 127
print(1 * pow(10,2) + 2 * pow (10, 1) + 7 * pow (10, 0 ))

#ДВОИЧНАЯ СИСТЕМА
# pow (2, 3) pow(2, 2) pow (2,1) pow(2,0)
x = 0b101
print(x)
print(1 * pow(2, 2) + 0 * pow (2,1) + 1 * pow(2,0))

y = 0b0110 #6
print(y)
print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow (2,1) + 0 * pow(2,0))

#ШЕСТНАДТИРИЧНАЯ СИСТЕМА

z = 0xffff
print(format(z, '0>42b'))
print(15 * pow (16, 1) + 1 * pow(16, 0))
print(0b000000000000000000000000001111111111111111)




###################################
#53. Запись двоичных файлов
#################################
print(termcolor.colored('\n53. Запись двоичных файлов', 'red'))

with open('test_binary', 'bw') as test_file:
    for number in range(21):
        test_file.write(bytes([number]))

#второй способ по проще
# with open('test_binary', 'bw') as test_file:
#     test_file.write(bytes(range(21)))


with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)

###################################
#54. Модуль pickle (мариновать консервировать)
#################################
print(termcolor.colored('\n54. Модуль pickle', 'red'))

import pickle

honda = (
    'civic',
    'grey',
    '2019',
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green'),
    )
)

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)


with open('honda.pickle', 'rb') as honda_file:
    honda_from_file = pickle.load(honda_file)

#print(honda_from_file)

model, color, year, owner_list = honda_from_file

print(model)
print(color)
print(year)
for owner in owner_list:
    owner_number, owner_name = owner
    print(owner_number, owner_name)

print('------------------')

models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White', 'Jake Green']

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(999999999, honda_file)

with open('honda.pickle', 'rb') as honda_retr:
    honda_from_file = pickle.load(honda_retr)
    models = pickle.load(honda_retr)
    owners = pickle.load(honda_retr)
    a = pickle.load(honda_retr)

print(honda_from_file)
print(models)
print(owners)
print(a)


##################################
#55. Модуль shelve
#################################
print(termcolor.colored('\n55. Модуль shelve', 'red'))

import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['opel'])

    for key in cars:
        print(key)


##################################
#56. Работа с данными при помощи модуля shelve
#################################
print(termcolor.colored('\n56. Работа с данными при помощи модуля shelve', 'red'))


with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['opel'])
    print(cars.get('ope'))

    cars['kia'] = 'Korea'

    for key in cars:
        print(key + ': ' + cars[key])

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     country = cars.get(key, 'We don\'t have a ' + key)
    #     print(country)

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     if key in cars:
    #         country = cars[key]
    #         print(country)
    #     else:
    #         print('We don\'t have a ' + key)

    print('+++')
    ordered_key_list = list(cars.keys())
    ordered_key_list.sort() #сортировка
    for key in ordered_key_list:
        print(key + ' ' + cars[key])

    for value in cars.values():
        print(value)
    print(cars.values())
    print(type(cars.values()))

    for key in cars.keys():
        print(key)
    print(cars.keys())
    print(type(cars.keys()))

    for item in cars.items():
        print(item)
    print(cars.items())
    print(type(cars.items()))
