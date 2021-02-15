#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 4. Создать класс Triangle для представления треугольника.
# Поля данных должны включать углы и стороны.
# Требуется реализовать операции: получения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

from individ2 import Triangle

if __name__ == '__main__':
    r1 = Triangle()
    r1.read()
    print(r1.per())
    print(r1.square())
    print(r1.height_one())
    print(r1.height_two())
    print(r1.height_three())
    print(r1.degrees())
