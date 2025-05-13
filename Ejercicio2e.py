from chessPictures import SQUARE
from interpreter import draw
from picture import Picture

blanco = Picture(SQUARE)
negro = blanco.negative()

# Alternamos negro y blanco, empezando con negro
fila = negro.join(blanco).horizontalRepeat(4)

draw(fila)
