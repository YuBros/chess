from piezas import Peon, Alfil, Caballo, Torre, Reina, Rey, Color

class TableroAjedrez:
    def __init__(self):
        self.tablero=[
            [Torre(Color.BLANCO, (0, 0)), Caballo(Color.BLANCO, (0, 1)), Alfil(Color.BLANCO, (0, 2)), Reina(Color.BLANCO, (0, 3)), Rey(Color.BLANCO, (0, 4)), Alfil(Color.BLANCO, (0, 5)), Caballo(Color.BLANCO, (0, 6)), Torre(Color.BLANCO, (0, 7))], 
            [Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO), Peon(Color.BLANCO)], 
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO), Peon(Color.NEGRO)], 
            [Torre(Color.NEGRO), Caballo(Color.NEGRO), Alfil(Color.NEGRO), Reina(Color.NEGRO), Rey(Color.NEGRO), Alfil(Color.NEGRO), Caballo(Color.NEGRO), Torre(Color.NEGRO)], 
        ]
    def mover_pieza(self, casilla_inicial, casilla_final):
        fila_inicial, columna_inicial=casilla_inicial
        pieza=self.tablero[fila_inicial][columna_inicial]
        self.tablero[fila_inicial][columna_inicial]=" "
        fila_final, columna_final=casilla_final
        self.tablero[fila_final][columna_final]=pieza


print("\n\n\n")
a=TableroAjedrez()
for fila in a.tablero:
    print(fila)

a.mover_pieza([0, 4], [3, 4])
print("\n\n\n")
for fila in a.tablero:
    print(fila)