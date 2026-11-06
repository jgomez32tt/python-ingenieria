import unittest

from calculadora_combustible import calcular_consumo


class TestCalcularConsumo(unittest.TestCase):
    def test_consumo_2400_galones_32_horas(self):
        resultado = calcular_consumo(2400, 32)
        self.assertEqual(resultado, 75.0)


if __name__ == "__main__":
    unittest.main()
