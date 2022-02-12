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
    color = None
    mark = None
    weight = None

    def __init__(self, brand, age, mark, weight, color):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("MOVE, Man!!!")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("Man, STOP!!!")


if __name__ == '__main__':
    auto_1 = Auto('Chrysler', 2005, '300C', 2225, 'black')
    print(auto_1.brand)
    print(auto_1.age)
    print(auto_1.mark)
    print(auto_1.weight)
    print(auto_1.color)
