from chessPictures import *
from interpreter import draw
from picture import Picture

knight = Picture(KNIGHT)
knight_neg = knight.negative()

fila1 = knight_neg.join(knight)
fila2 = knight.join(knight_neg)

tablero = fila1.under(fila2)

draw(tablero)