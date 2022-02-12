# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
import math


class Auto:
    brand = "Fiat Chrysler Automobiles"
    age = 2005
    color = "Black"
    mark = "Chrysler"
    weight = 2225

    def move(self):
        print("MOVE, Man!!!")

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("Man, STOP!!!")


if __name__ == '__main__':
    auto_1 = Auto()
    print(f"Brand auto --- {auto_1.brand}", f"Mark --- {auto_1.mark}", sep='\n')
    print()
    auto_1.move()
    auto_1.stop()
    print()
    print(auto_1.birthday())