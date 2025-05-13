from chessPictures import KNIGHT
from interpreter import draw
from picture import Picture

knight = Picture(KNIGHT)
knight_neg = knight.negative()

knight_right = knight.verticalMirror()
knight_neg_right = knight_neg.verticalMirror()

fila1 = knight_neg_right.join(knight_right)
fila2 = knight.join(knight_neg)

tablero = fila1.under(fila2)

draw(tablero)
