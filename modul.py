#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


class IllegalMarksError(Exception):

    def __init__(self, marks, message="Illegal marks number"):
        self.marks = marks
        self.message = message
        super(IllegalMarksError, self).__init__(message)

    def __str__(self):
        return f"{self.marks} -> {self.message}"


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):

    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class Person:
    name: str
    group: str
    marks: list[int]


@dataclass
class Staff:
    students: List[Person] = field(default_factory=lambda: [])

    def add(self, name, group, marks):
        self.students.append(
            Person(
                name=name,
                group=group,
                marks=marks
            )
        )
        self.students.sort(key=lambda person: person.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 11
        )
        table.append(line)
        table.append(
            '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "1-ая оценка",
                "2-ая оценка",
                "3-ая оценка",
                "4-ая оценка",
                "5-ая оценка"
            )
        )
        table.append(line)

        # Вывести данные о всех оценках ученика.
        for idx, person in enumerate(self.students, 1):
            table.append(
                '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                    idx,
                    person.name,
                    person.group,
                    person.marks[0],
                    person.marks[1],
                    person.marks[2],
                    person.marks[3],
                    person.marks[4]
                )
            )
        table.append(line)

        return '\n'.join(table)

    def __repr__(self):
        return self.__str__()

    def select(self):
        result = []
        count = 0
        for person in self.students:
            if sum(person.marks) / len(person.marks) > 4.0:
                count += 1
                result.append(person)
        return result
