import unittest
from src.jugador import jugador
from src.tateti import tateti

class TestTatetiJugador(unittest.TestCase):

    def setUp(self):
        self.j1 = jugador("Ana", "X")
        self.j2 = jugador("Luis", "O")
        self.juego = tateti(self.j1, self.j2)

    def test_jugador_inicial_turno(self):
        self.assertEqual(self.juego.turno, self.j1)

    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, self.j2)
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, self.j1)

    def test_jugador_nombre(self):
        self.assertEqual(self.juego.jugador1.nombre, "Ana")
        self.assertEqual(self.juego.jugador2.nombre, "Luis")

    def test_jugador_simbolo(self):
        self.assertEqual(self.juego.jugador1.simbolo, "X")
        self.assertEqual(self.juego.jugador2.simbolo, "O")

    def test_ocupar_casilla_jugador1(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.obtener_contenedor()[0][0], "X")

    def test_ocupar_casilla_jugador2(self):
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(self.juego.tablero.obtener_contenedor()[1][1], "O")

    def test_hay_ganador_horizontal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(0, 2)
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_hay_ganador_vertical(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(2, 0)
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_hay_ganador_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(0, 2)
        self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_empate(self):
        movimientos = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        for idx, (fila, col) in enumerate(movimientos):
            self.juego.ocupar_una_de_las_casillas(fila, col)
            if idx < len(movimientos) - 1:
                self.juego.cambiar_turno()
        self.assertTrue(self.juego.tablero.esta_lleno())
        self.assertFalse(self.juego.hay_ganador("X"))
        self.assertFalse(self.juego.hay_ganador("O"))

if __name__ == '__main__': 
    unittest.main()