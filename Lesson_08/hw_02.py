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


class truck(Auto):
    max_load = "4 long ton"
    trailer = "Yes"

    def move(self):
        print('ATTENTION!!!')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load...')
        time.sleep(1)
        print('...GO!')


class car(Auto):
    max_speed = 200
    tunning = "Chip"
    dors = 2

    def move(self):
        super().move()
        print(f'max speed is {Chrysler.max_speed} km/h!!!')


Chrysler = car()
truck_1 = truck()

Chrysler.move()
print("=" * 33)
print(f'Tun: {Chrysler.tunning}')
print(f'Dors: {Chrysler.dors}')
print("=" * 33)
truck_1.move()
print("=" * 33)
print(f'Load: {truck_1.max_load}')
print(f'Is there a trailer?', f'<<<{truck_1.trailer}>>>', sep='\n')
print("=" * 33)
truck_1.load()
print("=" * 34)
