from src.tablero import tablero
from src.jugador import jugador

class tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = self.jugador1
        self.tablero = tablero()

    def ocupar_una_de_las_casillas(self, fila, columna):
        # Pone la ficha del jugador actual
        self.tablero.poner_la_ficha(fila, columna, self.turno.simbolo)

    def cambiar_turno(self):
        # Cambia el turno al otro jugador
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1

    def hay_ganador(self, simbolo):
        contenedor = self.tablero.obtener_contenedor()

        # Verifica filas
        for fila in contenedor:
            if fila == [simbolo, simbolo, simbolo]:
                return True
            
        # Verifica columnas
        for columna in range(3):
            if [contenedor[fila][columna] for fila in range(3)] == [simbolo, simbolo, simbolo]:
                return True
            
        # Verifica diagonal principal
        if [contenedor[i][i] for i in range(3)] == [simbolo, simbolo, simbolo]:
            return True
        
        # Verifica diagonal secundaria
        if [contenedor[i][2 - i] for i in range(3)] == [simbolo, simbolo, simbolo]:
            return True
        return False

    def hay_empate(self):
        # Empate si el tablero está lleno y no hay ganador
        return self.tablero.esta_lleno() and not (
            self.hay_ganador(self.jugador1.simbolo) or self.hay_ganador(self.jugador2.simbolo)
        )