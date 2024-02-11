from enum import StrEnum
from tblero import TableroAjedrez
class Pieza:
    def __init__(self,color):
        self.color=color
    def can_move(self,
                from_position: tuple[int,int],
                new_board:tuple[int,int],
                tblero:TableroAjedrez
                )-> bool:
        row,column=new_board
        if tblero.tablero [column][row].color ==self.color:
            return False
        return True

class Color(StrEnum):
    BLANCO="blanco"
    NEGRO="negro"

class Peon(Pieza):
    def can_move(self,
                 from_position: tuple[int,int],
                 new_board:tuple[int,int],
                 tblero:TableroAjedrez)-> bool:
        if not super().can_move(from_position, new_board, tblero):
            return False
class Alfil(Pieza):
    ...

class Caballo(Pieza):
    ...

class Torre(Pieza):
    ...

class Reina(Pieza):
    ...

class Rey(Pieza):
    ...