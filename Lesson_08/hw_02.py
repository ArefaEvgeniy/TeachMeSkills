# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Создать по 2 объекта для каждого из классов
# truck и car, проверить все их методы и атрибуты.
from hw_01 import Auto
import time


class Truck(Auto):
    max_load = None
    trailer = None

    def __init__(self, brand, age, mark, max_load, trailer, weight, color):
        super().__init__(brand, age, mark, weight, color)
        self.max_load = max_load
        self.trailer = trailer

    def move(self):
        print('ATTENTION!!!')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load...')
        time.sleep(1)
        print('...GO!')


class Car(Auto):
    max_speed = None
    tunning = None
    dors = None

    def __init__(self, brand, age, mark, max_speed, weight, color):
        super().__init__(brand, age, mark, weight, color)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {Chrysler.max_speed} km/h!!!')


Chrysler = Car('Chrysler', 2005, '300C', 300, 2225, 'Black')
print('*' * 54)
print(Chrysler.brand, Chrysler.mark, Chrysler.age, f'{Chrysler.max_speed} km/h', Chrysler.weight, Chrysler.color,
      sep='-|-')
print('*' * 54)
Chrysler.move()
print('*' * 54)
Chrysler.stop()
print('*' * 54)

Volvo = Truck('Volvo', 'F-456G', 2019, "4 long ton", "Yes", 5578, 'Yellow')
print(Volvo.brand, Volvo.mark, Volvo.age, Volvo.max_load, f'(There is a trailer?) - {Volvo.trailer}', Volvo.weight,
      Volvo.color, sep='-|-')
print('*' * 54)
Volvo.move()
print('*' * 54)
Volvo.load()
print('*' * 54)
