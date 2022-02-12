Здесь всё отлично - молодец!
# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.


import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)


class Circle(Point):
    radius = 0

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return 'Circle' + super().__str__()[5:-1] + f', radius: {self.radius})'

    def __sub__(self, other):
        point = super().__sub__(other)
        radius = self.radius - other.radius
        return Point(point.x, point.y) if self.radius == other.radius else Circle(abs(radius), point.x, point.y)


a = Circle(3, 1, 1)
print(a)

b = Circle(2, 5, 7)
print(b)

print(a - b)
