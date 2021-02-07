import Equacao_quadratica
import pytest

class TestaValores:

    @pytest.mark.parametrize("coeficiente_a, coeficiente_b, coeficiente_c, valor_esperado",[
        (2,4,2,(1,-1)),
        (3,4,9,False),
        (2,5,2,(2,-0.5,-2))
    ])
    def testa_valores(self, coeficiente_a, coeficiente_b, coeficiente_c, valor_esperado):
        calcular = Equacao_quadratica.Equacao_Quadratica(coeficiente_a, coeficiente_b, coeficiente_c)
        assert calcular.calcular_delta() == valor_esperado