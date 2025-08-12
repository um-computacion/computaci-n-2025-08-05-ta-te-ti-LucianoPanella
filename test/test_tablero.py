import unittest
from src.tablero import tablero

class TestTablero(unittest.TestCase):

    def test_tablero_inicial_vacio(self):
        t = tablero()
        contenedor = t.obtener_contenedor()
        for fila in contenedor:
            for casillero in fila:
                self.assertEqual(casillero, "")

    def test_poner_ficha(self):
        t = tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.obtener_contenedor()[0][0], "X")

    def test_poner_varias_fichas(self):
        t = tablero()
        t.poner_la_ficha(1, 1, "O")
        t.poner_la_ficha(2, 2, "X")
        contenedor = t.obtener_contenedor()
        self.assertEqual(contenedor[1][1], "O")
        self.assertEqual(contenedor[2][2], "X")

    def test_casillero_ocupado(self):
        t = tablero()
        t.poner_la_ficha(0, 1, "X")
        self.assertNotEqual(t.obtener_contenedor()[0][1], "")

    def test_esta_lleno_false(self):
        t = tablero()
        self.assertFalse(t.esta_lleno())

    def test_esta_lleno_true(self):
        t = tablero()
        for i in range(3):
            for j in range(3):
                t.poner_la_ficha(i, j, "X")
        self.assertTrue(t.esta_lleno())

    def test_obtener_casillero(self):
        t = tablero()
        t.poner_la_ficha(2, 1, "O")
        self.assertEqual(t.obtener_contenedor()[2][1], "O")

    def test_obtener_casillero_vacio(self):
        t = tablero()
        self.assertEqual(t.obtener_contenedor()[1][2], "")

    def test_mostrar_tablero_no_excepcion(self):
        t = tablero()
        try:
            t.mostrar_tablero()
        except Exception as e:
            self.fail(f"mostrar_tablero() lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()