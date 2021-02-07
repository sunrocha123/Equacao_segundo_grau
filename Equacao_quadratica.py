import math
import pytest

class Equacao_Quadratica:

    def __init__(self, coeficiente_a, coeficiente_b, coeficiente_c):
        self.coeficiente_a = coeficiente_a
        self.coeficiente_b = coeficiente_b
        self.coeficiente_c = coeficiente_c

    def calcular_delta(self):
        delta = math.pow(self.coeficiente_b,2) - 4 * self.coeficiente_a * self.coeficiente_c

        if delta < 0:
            return False
        else:
            return self.raizes(delta)

    def raizes(self, delta):
        raiz1 = (-(self.coeficiente_b) + math.sqrt(delta)) / (2 * self.coeficiente_a)
        raiz2 = (-(self.coeficiente_b) - math.sqrt(delta)) / (2 * self.coeficiente_a)

        if delta == 0:
            return 1, raiz1
        else:
            return 2, raiz1, raiz2