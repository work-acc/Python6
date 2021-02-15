#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 4. Создать класс Triangle для представления треугольника.
# Поля данных должны включать углы и стороны.
# Требуется реализовать операции: получения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

import math


class Triangle:

    def __init__(self, first=1, second=1, third=1):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

        self.__corner_one()

    # Ввод сторон треугольника
    def read(self):
        first = input('Введите первую сторону треугольника: ')
        second = input('Введите вторую сторону треугольника: ')
        third = input('Введите третью сторону треугольника: ')

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

        self.__corner_one()

    # Вычисление периметра треугольника
    def per(self):
        return self.first + self.second + self.third

    # Вычисление площади треугольника
    def square(self):
        p = self.per() / 2
        return math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))

    # Вычисление высоты проведенной к стороне A
    def height_one(self):
        p = self.per() / 2
        return 2 * (math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))) / self.first

    # Вычисление высоты проведенной к стороне B
    def height_two(self):
        p = self.per() / 2
        return 2 * (math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))) / self.second

    # Вычисление высоты проведенной к стороне C
    def height_three(self):
        p = self.per() / 2
        return 2 * (math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))) / self.third

    # Вычисление градусов углов по формуле Герона
    def __corner_one(self):
        a = self.first
        b = self.second
        c = self.third
        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.f_d = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.s_d = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.th_d = math.degrees(third_corner)

    # Вывод углов
    def degrees(self):
        if self.f_d == 90 or self.s_d == 90 or self.th_d == 90:
            return print("Треугольник прямоугольный")
        elif self.f_d == self.s_d or self.f_d == self.th_d or self.s_d == self.th_d:
            return print("Треугольник равнобедренный")
        elif self.f_d == self.s_d == self.th_d:
            return print("Треугольник равносторонний")
        else:
            return print("Обычный треугольник")