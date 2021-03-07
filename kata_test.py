import unittest
from unittest import mock

from kata import CodeKataPython2, CodeKataPython3, global_function_python2, global_function_python3


class CodeKataPython2Test(unittest.TestCase):

    def setUp(self):
        self.code_kata = CodeKataPython2()

    @mock.patch('kata.randint')
    def test_test_method(self, mock_randint):
        mock_randint.return_value = 1
        self.assertEqual(self.code_kata.random_from_list([10, 20]), 20)


class GlobaLPython2Test(unittest.TestCase):

    def test_test(self):
        self.assertEqual(global_function_python2(), 'my_test')


class CodeKataPython3Test(unittest.TestCase):

    def setUp(self):
        self.code_kata = CodeKataPython3()

    @mock.patch('kata.randint')
    def test_test_method(self, mock_randint):
        mock_randint.return_value = 1
        self.assertEqual(self.code_kata.random_from_list([10, 20]), 20)


class GlobaLPython3Test(unittest.TestCase):

    def test_test(self):
        self.assertEqual(global_function_python3(), 'my_test')
