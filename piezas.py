from enum import StrEnum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tblero import TableroAjedrez
class Pieza:
    def __init__(self,color):
        self.color=color
    def can_move(self,
                from_position: tuple[int,int],
                new_position:tuple[int,int],
                tblero:'TableroAjedrez'
                )-> bool:
        row,column=new_position
        if tblero.tablero [column][row].color ==self.color:
            return False
        return True

class Color(StrEnum):
    BLANCO="blanco"
    NEGRO="negro"

class Peon(Pieza):
    def can_move(self,
                 from_position: tuple[int,int],
                 new_position:tuple[int,int],
                 tblero:'TableroAjedrez')-> bool:
        if not super().can_move(from_position, new_position, tblero):
            return False
        from_row, from_column =from_position
        to_row, to_column= new_position
        row=abs(to_row-from_row)
        column=abs(to_column-from_column)
        if (
            row>2 
            or row<0 
            or (row==1 and tblero[to_row][to_column] != " " and column == 0)
        ):
            return False
        return True 
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