import unittest
from models.carga_model import CargaModel

class TestCargaModel(unittest.TestCase):
    def test_criacao(self):
        carga = CargaModel("areia", 1000, "porto")
        self.assertEqual(carga.nome, "areia")
        self.assertEqual(carga.peso, 1000)
        self.assertEqual(carga.destino, "porto")

if __name__ == '__main__':
    unittest.main()
