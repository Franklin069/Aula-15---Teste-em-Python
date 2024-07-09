# Importando o pacote de testes unitários
import unittest

# Importando a classe 'Calculadora' pelo arquivo 'calculadora.py'
from calculadora import Calculadora

# Criando a classe de testes unitários chamada 'TestCalculadora'
class TestCalculadora(unittest.TestCase):

    # Criando o método de definição do objeto que herdará a classe 'Calculadora'
    # chamado 'setUp'
    def setUp(self):
        self.calc = Calculadora()

        # Criando o teste do método 'soma' da classe 'Calculadora'
        def test_soma(self):
            self.assertEqual(self.calc.soma(10, 20), 30)
             

# Chamando a classe de Testes Unitários
if __name__ == '__main__':
    unittest.main()
