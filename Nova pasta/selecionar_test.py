from unittest import TestCase
from selecionar import *

class TestListar(TestCase):


    def abrir_foto(self):
        self.assertRaises(abrirfoto)  # test strings
        self.assertRaises(TypeError, area_of_a_triangle, 2, None)