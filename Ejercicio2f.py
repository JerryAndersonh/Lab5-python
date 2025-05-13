from chessPictures import SQUARE
from interpreter import draw
from picture import Picture

blanco = Picture(SQUARE)
negro = blanco.negative()

# Fila que empieza en blanco
fila_blanco = blanco.join(negro).horizontalRepeat(4)

# Fila que empieza en negro
fila_negro = negro.join(blanco).horizontalRepeat(4)

# Alternamos las filas
tablero = fila_negro.under(fila_blanco).under(fila_negro).under(fila_blanco)

draw(tablero)
