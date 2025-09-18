#escrevendo testes unitarios
import unittest

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return x / y

class TestOperacoes(unittest.TestCase):

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 4), 12)
        self.assertEqual(multiplica(-1, 5), -5)
        self.assertEqual(multiplica(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
    
    def test_divide_por_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

#agora depure usando print, e em seguida, com o operador pdb
def soma(a, b):
    print(f"Somando {a} e {b}")
    resultado = a + b
    print(f"Resultado: {resultado}")
    return resultado

import pdb
def soma_com_pdb(a, b):
    pdb.set_trace()
    resultado = a + b
    return resultado
resultado=soma(2, 3)
print(resultado)