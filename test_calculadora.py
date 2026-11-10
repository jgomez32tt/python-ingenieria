import unittest

from calculadora_combustible import calcular_consumo


class TestCalcularConsumo(unittest.TestCase):
    def test_consumo_2400_galones_32_horas(self):
        resultado = calcular_consumo(2400, 32)
        self.assertEqual(resultado, 75.0)

    def test_horas_iguales_a_cero(self):
        with self.assertRaises(ValueError):
            calcular_consumo(10, 0)

    def test_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_consumo(10, -1)

    def test_galones_negativos(self):
        with self.assertRaises(ValueError):
            calcular_consumo(-1, 2)


if __name__ == "__main__":
    unittest.main()
