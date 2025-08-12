import unittest
from unittest.mock import patch
from src import cli

class TestCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '0', '1', '0', '2'])
    @patch('builtins.print')
    def test_ganador_horizontal(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("¡El ganador es" in str(call) for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '1', '0', '2', '0'])
    @patch('builtins.print')
    def test_ganador_vertical(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("¡El ganador es" in str(call) for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '1', '1', '2', '2'])
    @patch('builtins.print')
    def test_ganador_diagonal(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("¡El ganador es" in str(call) for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '0', '1', '0', '2', '1', '1', '1', '0', '1', '2', '2', '1', '2', '0', '2', '2'])
    @patch('builtins.print')
    def test_empate(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("empate" in str(call).lower() for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '3', '0', '0', '0'])
    @patch('builtins.print')
    def test_movimiento_fuera_de_rango(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("fuera del tablero" in str(call).lower() or "no es permitido" in str(call).lower() for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '0', '0', '1', '1'])
    @patch('builtins.print')
    def test_casillero_ocupado(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("ya ocupado" in str(call).lower() for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', 'a', '0', '0', '0'])
    @patch('builtins.print')
    def test_input_invalido(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("invalid" in str(call).lower() or "no es permitido" in str(call).lower() or "literal" in str(call).lower() for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '-1', '0', '0', '0'])
    @patch('builtins.print')
    def test_movimiento_negativo(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("fuera del tablero" in str(call).lower() or "no es permitido" in str(call).lower() for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '0', '1', '0', '2'])
    @patch('builtins.print')
    def test_nombre_jugadores(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("Turno de Ana" in str(call) or "Turno de Luis" in str(call) for call in mock_print.call_args_list))

    @patch('builtins.input', side_effect=['Ana', 'Luis', '0', '0', '0', '1', '0', '2'])
    @patch('builtins.print')
    def test_muestra_tablero(self, mock_print, mock_input):
        cli.main()
        self.assertTrue(any("Tablero:" in str(call) for call in mock_print.call_args_list))

if __name__ == '__main__':
    unittest.main()