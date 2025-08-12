import unittest
from src.jugador import jugador

class TestJugador(unittest.TestCase):

    def test_crear_jugador_nombre_y_simbolo(self):
        j = jugador("Ana", "X")
        self.assertEqual(j.nombre, "Ana")
        self.assertEqual(j.simbolo, "X")

    def test_jugador_nombre_vacio(self):
        j = jugador("", "O")
        self.assertEqual(j.nombre, "")

    def test_jugador_simbolo_minuscula(self):
        j = jugador("Luis", "o")
        self.assertEqual(j.simbolo, "o")

    def test_jugador_simbolo_distinto(self):
        j = jugador("Pepe", "#")
        self.assertEqual(j.simbolo, "#")

    def test_jugador_nombre_con_espacios(self):
        j = jugador("Juan Perez", "X")
        self.assertEqual(j.nombre, "Juan Perez")

    def test_jugador_simbolo_numerico(self):
        j = jugador("Nico", "1")
        self.assertEqual(j.simbolo, "1")

    def test_jugador_nombre_largo(self):
        nombre_largo = "a" * 100
        j = jugador(nombre_largo, "O")
        self.assertEqual(j.nombre, nombre_largo)

    def test_jugador_simbolo_vacio(self):
        j = jugador("Ana", "")
        self.assertEqual(j.simbolo, "")

    def test_jugador_str(self):
        j = jugador("Ana", "X")
        self.assertTrue(isinstance(str(j), str))

    def test_jugador_igualdad(self):
        j1 = jugador("Ana", "X")
        j2 = jugador("Ana", "X")
        self.assertEqual(j1.nombre, j2.nombre)
        self.assertEqual(j1.simbolo, j2.simbolo)

if __name__ == '__main__':
    unittest.main()