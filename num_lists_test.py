"""
Модуль тестирования классов NumLists
"""
import io
import sys
import unittest

from unittest.mock import patch, PropertyMock

from num_lists_controller import NumListsController
from num_lists_model import NumListsModel


class NumListsTest(unittest.TestCase):
    """
    Тестирование методов класса NumListsModel и NumListsController
    """

    __slots__ = ['model', 'ctrl']

    def setUp(self) -> None:
        """
        Инициализация экземпляров классов перед тестом
        """
        self.model = NumListsModel()
        self.ctrl = NumListsController()

    def tearDown(self) -> None:
        """
        Очистка экземпляров классов после тестом
        """
        del self.model
        del self.ctrl

    def test_default_splitter(self):
        """
        Тестирование наличия стандартного сплиттера.
        Сверяем с помощью assertEqual
        """
        self.assertEqual(self.model.splitter, ' ')

    def test_alt_splitter(self):
        """
        Тестирование установки альтернативного сплиттера.
        Сверяем с помощью assertEqual
        """
        self.model.splitter = '#'
        self.assertEqual(self.model.splitter, '#')

    def test_input_num_list_str_std_splitter(self):
        """
        Тестируем преобразование корректной строки со стандартным сплиттером.
        Метод класса должен возвращать list[float].
        С помощью assertEqual сверяем список.
        Базовый сценарий работы метода со стандартным сплиттером.
        """
        self.assertEqual(self.model.input_num_list('1.1 2.2 3.3'),
                         [1.1, 2.2, 3.3])

    @patch('num_lists_test.NumListsModel._splitter', return_value=',',
           new_callable=PropertyMock)
    def test_input_num_list_str_alt_splitter(self, _mocked):
        """
        Тестируем преобразование корректной строки с альтернативным сплиттером.
        Метод класса должен возвращать list[float].
        Splitter задаем моком.
        С помощью assertEqual свеояем список.
        """
        self.assertEqual(self.model.input_num_list('1.1, 2.2, 3.3'),
                         [1.1, 2.2, 3.3])

    def test_input_num_list_str_instanse(self):
        """
        Тестируем преобразование в корректный тип.
        Метод класса должен возвращать list[float].
        С помощью assertIsInstance проверяем тип данных.
        """
        self.assertIsInstance(self.model.input_num_list('1')[0],
                              float)

    def test_input_num_list_str_valerror(self):
        """
        Тестируем преобразование некорректной строки
        и возникновения ValueError.
        Метод класса должен возвращать None.
        С помощью assertIsNone проверяем ответ.
        """
        self.assertIsNone(self.model.input_num_list('O 1'))

    def test_input_num_list_str_attrerror(self):
        """
        Тестируем преобразование некорректной строки
        и возникновения AttributeError.
        Метод класса должен возвращать None.
        С помощью assertIsNone проверяем ответ.
        """
        self.assertIsNone(self.model.input_num_list(None))

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           return_value='1.1 2.2')
    def test_get_list(self, _mocked):
        """
        Тестируем получение списка чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем получен ли верный список или нет
        """
        self.model.push_list()
        self.assertEqual(self.model.get_list(0), [1.1, 2.2])

    def test_get_list_indexerror(self):
        """
        Тестируем получение несуществующего списка чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем получен ли верный список или нет
        """
        self.assertIsNone(self.model.get_list(0))

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_push_list(self, _mocked):
        """
        Тестируем добавление списка чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем добавлен ли список или нет
        """
        self.model.push_list()
        self.model.push_list()
        self.model.push_list()
        self.assertEqual(self.model.get_list(2), [3.3, 4.4])

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_del_list(self, _mocked):
        """
        Тестируем удаление списка чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual возврат следующего за удаленным списка
        """
        self.model.push_list()
        self.model.push_list()
        self.model.push_list()
        self.model.del_list(1)
        self.assertEqual(self.model.get_list(1), [3.3, 4.4])

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_del_list_indexerror(self, _mocked):
        """
        Тестируем удаление несуществующего списка чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем количество списков.
        """
        self.model.push_list()
        self.model.push_list()
        self.model.push_list()
        self.model.del_list(3)
        self.assertEqual(self.model.count_lists, 3)

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_count_list(self, _mocked):
        """
        Тестируем подсчет списков чисел.
        Ввод с клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем возврат следующего за удаленным списка
        """
        self.model.push_list()
        self.model.push_list()
        self.model.push_list()
        self.assertEqual(self.model.count_lists, 3)

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_count_mean(self, _mocked):
        """
        Тестируем получение среднего из списка чисел.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем возврат корректного среднего
        """
        self.model.push_list()
        self.model.push_list()
        self.model.push_list()
        self.assertEqual(self.model.get_list_mean(1), 2.75)

    def test_count_mean_indexerror(self):
        """
        Тестируем получение среднего из списка чисел по ошибочному индексу.
        Методом assertIsNone проверяем возврат None
        """
        self.assertIsNone(self.model.get_list_mean(1))

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2', '2.2 3.3', '3.3 4.4'])
    def test_controller_run_two_lists(self, _mocked):
        """
        Тестируем получение двух списков чисел при запуске приложения.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем корректность значения
        """
        self.ctrl.run()
        self.assertEqual(self.ctrl.num_lists.count_lists, 2)

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2 3.3', '1.1 22.22 -16.72'])
    def test_controller_run_equals(self, _mocked):
        """
        Тестируем обработку двух списков с равными средними.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем корректность значения
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ctrl.run()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         'Средние значения равны')

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2 3.3001', '1.1 2.2 3.3'])
    def test_controller_run_bigger(self, _mocked):
        """
        Тестируем обработку со средним большим у первого списка.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем корректность значения
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ctrl.run()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         'Первый список имеет большее среднее значение')

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2 3.3001', '1.1 2.2 3.3002'])
    def test_controller_run_lower(self, _mocked):
        """
        Тестируем обработку со средним большим у первого списка.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем корректность значения
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ctrl.run()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         'Второй список имеет большее среднее значение')

    @patch('num_lists_test.NumListsModel._input_num_list_str',
           side_effect=['1.1 2.2 3.3', '1.1 22.22 -16.72'])
    def test_controller_run_cleanup(self, _mocked):
        """
        Тестируем очистку списков.
        Ввод клавиатуры заменяем заглушкой.
        Методом assertEqual проверяем корректность значения
        """
        self.ctrl.run()
        self.ctrl.clean_up()
        self.assertEqual(self.ctrl.count_lists, 0)


if __name__ == '__main__':
    unittest.main()
