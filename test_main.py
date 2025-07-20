import unittest
from main import texto_api

class TestsProductos(unittest.TestCase):
    def test_datos(self):
        data = [
            {
                "id": 1,
                "name": "iPhone 13",
                "description": "The latest iPhone from Apple",
                "price": 999.99,
                "currency": "USD",
                "in_stock": True
            }
        ]
        salida = texto_api(data)
        self.assertIn("iPhone 13", salida)

    def test_sin_datos(self):
        data = []
        salida = texto_api(data)
        self.assertEqual(salida, "Nada que mostrar.")

if __name__ == "__main__":
    unittest.main()