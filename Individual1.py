#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 1. Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по возрастанию номера группы; вывод на
# дисплей фамилий и номеров групп для всех студентов, включенных в массив, если средний
# балл студента больше 4.0; если таких студентов нет, вывести соответствующее сообщение.

import modul
import logging
import sys


if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='workers.log',
        format='[%(asctime)s] [%(levelname)s] => %(message)s',
        level=logging.INFO
    )

    # Список студентов.
    staff = modul.Staff()
    # Организовать бесконечный цикл запроса команд.
    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                # Запросить данные о студенте.
                name = input("Введите фамилию и инициалы: ")
                group = input("Введите группу: ")
                marks = list(map(int, input("Введите пять оценок в формате - 1,2,3: ").split(',')))
                # Добавить студентов.
                staff.add(name, group, marks)
                logging.info(
                    f"Добавлен студент: {name}, {group}, "
                    f"получивший оценки {marks}"
                )

                for number in marks:
                    if 5 > number < 2:
                        print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                        exit(1)

            elif command == 'list':
                # Вывести список.
                print(staff)
                logging.info("Отображен список студентов.")

            elif command == 'list':
                # Вывести список.
                print(staff)
                logging.info("Отображен список студентов.")

            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=2)
                # period = float(parts[1])
                # Запросить учеников.
                selected = staff.select()
                # Вывести результаты запроса.
                if selected:
                    for count, person in enumerate(selected, 1):
                        print(
                            '{:>3}: {}, {}'.format(count, person.name, person.group)
                        )
                    logging.info(
                        f"Найдено {len(selected)} студентов с "
                        f"средним баллом {parts[1]}"
                    )
                else:
                    print("Нет студентов, которые получили средний балл выше 4.0")
                logging.warning(
                    f"Студенты получившие средний балл {parts[1]} не найдены."
                )

            elif command == 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить студента;")
                print("list - вывести список студентов;")
                print("select <оценка> - найти студентов ;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            else:
                raise modul.UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)