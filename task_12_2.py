from math import pi, sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    @property
    def perimeter(self):
        return

    @property
    def square(self):
        return


class Circle(Figure):
    def __init__(self, central_point, radius):
        self.radius = radius
        self.central_point = central_point

    def __str__(self):
        return f'Perimeter of circle: {self.perimeter}\n' \
               f'Square of circle: {self.square}'

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def square(self):
        return pi * (self.radius ** 2)


class Triangle(Figure):
    def __init__(self, point_a, point_b, point_c):
        self.line_a_b = sqrt(((point_a.x - point_b.x) ** 2) + ((point_a.y - point_b.y) ** 2))
        self.line_a_c = sqrt(((point_a.x - point_c.x) ** 2) + ((point_a.y - point_c.y) ** 2))
        self.line_b_c = sqrt(((point_b.x - point_c.x) ** 2) + ((point_b.y - point_c.y) ** 2))

    def __str__(self):
        return f'Perimeter of triangle: {self.perimeter}\n' \
               f'Square of triangle: {self.square}'

    @property
    def perimeter(self):
        return self.line_b_c + self.line_a_c + self.line_a_b

    @property
    def square(self):
        return (
            sqrt((self.line_b_c + self.line_a_c + self.line_a_b) / 2 *
                 ((self.line_b_c + self.line_a_c + self.line_a_b) / 2 - self.line_a_b) *
                 ((self.line_b_c + self.line_a_c + self.line_a_b) / 2 - self.line_a_c) *
                 ((self.line_b_c + self.line_a_c + self.line_a_b) / 2 - self.line_b_c))
        )


class Square(Figure):
    def __init__(self, point_a, point_b):
        self.diagonal = sqrt(((point_a.x - point_b.x) ** 2) + ((point_a.y - point_b.y) ** 2))
        self.side = self.diagonal / sqrt(2)

    def __str__(self):
        return f'Perimeter of square: {self.perimeter}\n' \
               f'Square of square: {self.square}'

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def square(self):
        return self.side ** 2
