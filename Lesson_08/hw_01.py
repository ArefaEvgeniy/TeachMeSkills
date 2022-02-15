# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
import math


class Auto:
    brand = None
    age = None
    color = 'Black'
    mark = None
    weight = 2225

<<<<<<< HEAD
    def __init__(self, brand, mark, age):
=======
    def __init__(self, brand, age, mark, weight, color):  # так у вас все атрибуты должны быть обязательными, а в задании указаны только brand, age и mark 
>>>>>>> 4075058604421229b9ab736489cc1b27f397d1ed
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("MOVE, Man!!!")

    def birthday(self):
        self.age += 1
        return self.age

    def stop(self):
        print("Man, STOP!!!")


if __name__ == '__main__':
    Auto_1 = Auto('Chrysler', '300C', 2005)
    print(Auto_1.brand)
    print('*' * 54)
    print(Auto_1.birthday())
    print('*' * 54)
    print(Auto_1.mark)
    print('*' * 54)
    print(Auto_1.weight)
    print('*' * 54)
    print(Auto_1.color)
    print('*' * 54)
