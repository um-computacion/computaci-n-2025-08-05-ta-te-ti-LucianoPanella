from src.tateti import tateti
from src.tablero import tablero
from src.excepciones import (CasilleroOcupadoError, MovimientoInvalidoError)
from src.jugador import jugador

def main():
    print("Bienvenidos al Tateti")
    nombre1 = input("Ingrese el nombre del jugador 1 (ficha X): ")
    nombre2 = input("Ingrese el nombre del jugador 2 (ficha O): ")
    jugador1 = jugador(nombre1, "X")
    jugador2 = jugador(nombre2, "O")
    juego = tateti(jugador1, jugador2)
    while True:
        print("Tablero:")
        juego.tablero.mostrar_tablero()
        print(f"Turno de {juego.turno.nombre} (ficha: {juego.turno.simbolo})")
        try:
            fila = int(input("Ingrese fila (0-2): "))

            columna = int(input("Ingrese columna (0-2): "))

            juego.ocupar_una_de_las_casillas(fila, columna)
            
            if juego.hay_ganador(juego.turno.simbolo):
                juego.tablero.mostrar_tablero()
                print(f"¡El ganador es {juego.turno.nombre}!")
                break
            elif juego.tablero.esta_lleno():
                juego.tablero.mostrar_tablero()
                print("El juego ha terminado en empate.")
                break
            juego.cambiar_turno()

        except MovimientoInvalidoError:
            print("El movimiento está fuera del tablero o no es permitido. Intente de nuevo.")

        except CasilleroOcupadoError:
            print("Se intenta jugar en un casillero ya ocupado. Elija otra.")

        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()