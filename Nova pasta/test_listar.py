from unittest import TestCase
from listar import listardiretorio

class TestListar(TestCase):


    def test_nulls(self):
        self.assertRaises(ValueError, listardiretorio)  # test strings
        #self.assertRaises(TypeError, area_of_a_triangle, 2, None)
        self.assertRaises(TypeError, area_of_a_triangle, 2, None)

