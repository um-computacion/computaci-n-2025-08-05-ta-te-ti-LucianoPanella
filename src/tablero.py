from src.excepciones import CasilleroOcupadoError, MovimientoInvalidoError

class tablero:
    def __init__(self):
        self.__contenedor = [
            ["", "", ""],  # fila 0
            ["", "", ""],  # fila 1
            ["", "", ""]  # fila 2
        ]

    def poner_la_ficha(self, fila, columna, ficha):
        if fila < 0 or fila > 2 or columna < 0 or columna > 2:
            raise MovimientoInvalidoError("Fila o columna fuera de rango")
        if self.__contenedor[fila][columna] == "":
            self.__contenedor[fila][columna] = ficha
        else:
            raise CasilleroOcupadoError("La posición ya está ocupada")

    def obtener_contenedor(self):
        return self.__contenedor

    def mostrar_tablero(self):
        for fila in self.__contenedor:
            print(fila)

    def esta_lleno(self):
        for fila in self.__contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        return True