"""
Модуль класса модели данных списка чисел
"""

from typing import Optional


class NumListsModel:
    """
    Модель данных список чисел
    """
    __slots__ = ['_lists', '_splitter']

    def __init__(self):
        """
        Конструктор класса
        """
        self._lists = []
        self._splitter: str = ' '

    def _input_num_list_str(self) -> Optional[str]:
        """
        Выводит запрос на ввод строки со списком чисел и возвращает ввод.
        Аргументы:
            Не требуется
        Возвращает:
            None или str
        """
        return input(
            'Введите список чисел, разделенных пробелом. ' +
            f'Используйте символ "{self._splitter}" как ' +
            'разделитель целой и дробной части:\n>>')

    def input_num_list(self, list_str: str) -> Optional[list[float]]:
        """
        Преобразует строку с числами, разделенные пробелами в список чисел.
        Аргументы:
            list_str: str           - строка с числами, разделенными пробелами
        Возвращает:
            None или list[float]
        """
        try:
            return [float(num) for num in list_str.split(self._splitter)]
        except ValueError:
            # Ошибка преобразования во float. Игнорируем.
            # Если надо, то пишем в лог об ошибке
            pass
        except AttributeError:
            # В аргументе нет строки. Игнорируем
            # Если надо, то пишем в лог об ошибке
            pass
        return None

    def push_list(self) -> None:
        """
        Добавляет введенный с клавиатуры список чисел, если он не пустой
        """
        current_list = self.input_num_list(self._input_num_list_str())
        if current_list is not None:
            self._lists.append(current_list)

    def get_list(self, index: int) -> list[float]:
        """
        Возврашает список чисел по его индексу, если такой существует.
        В противном случае возвращает None
        Аргументы:
            index:int               - номер списка
        Возвращает:
            None или list[float]
        """
        try:
            return self._lists[index]
        except IndexError:
            return None

    def del_list(self, index) -> None:
        """
        Удаляет список чисел по его индексу
        Аргументы:
        Аргументы:
            index:int               - номер списка
        Возвращает:
            None
        """
        try:
            del self._lists[index]
        except IndexError:
            pass

    def get_list_mean(self, index: int) -> Optional[float]:
        """
        Вычисляет среднее значение из указанного списка
        Аргументы:
            index:int               - номер списка
        Возвращает:
            None или float
        """
        try:
            size: int = len(self._lists[index])
        except IndexError:
            return None
        summ: float = 0
        for i in range(size):
            summ += self._lists[index][i]
        return summ / size

    @property
    def splitter(self) -> str:
        """
        Возвращает сплиттер
        """
        return self._splitter

    @splitter.setter
    def splitter(self, value: str) -> None:
        """
        Устанавливает сплиттер
        """
        self._splitter = value

    @property
    def count_lists(self) -> int:
        """
        Возвращает количество введенных списков
        Аргументы:
            Отсутствуют
        Возвращает:
            int
        """
        return len(self._lists)
