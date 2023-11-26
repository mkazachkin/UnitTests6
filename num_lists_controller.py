"""
Модуль контроллера сравнения двух списков чисел
"""

from num_lists_model import NumListsModel


class NumListsController:
    """
    Контроллер сравнения двух списков чисел
    """
    __slots__ = ['num_lists']

    def __init__(self):
        """
        Конструктор класса
        """
        self.num_lists = NumListsModel()

    def run(self) -> None:
        """
        Запрашивает ввод данных и выполняет сравнение
        средних значений двух списков чисел.
        Из-за особенностей реализации типа данных float
        для сравнения среднее округляется до 8 знака после
        запятой.
        """
        while self.num_lists.count_lists != 1:
            self.num_lists.push_list()
        while self.num_lists.count_lists != 2:
            self.num_lists.push_list()
        # Особенности типа данных float.
        # Будем округлять до 8 знача после запятой
        mean_0: float = round(self.num_lists.get_list_mean(0), 8)
        mean_1: float = round(self.num_lists.get_list_mean(1), 8)
        if mean_0 == mean_1:
            print('Средние значения равны')
        elif mean_0 > mean_1:
            print(
                'Первый список имеет большее среднее значение')
        else:
            print(
                'Второй список имеет большее среднее значение')

    def clean_up(self) -> None:
        """
        Выполняет очистку списков чисел.
        """
        while self.num_lists.count_lists > 0:
            self.num_lists.del_list(0)

    @property
    def count_lists(self) -> int:
        """
        Возвращает количество списков чисел
        """
        return self.num_lists.count_lists
