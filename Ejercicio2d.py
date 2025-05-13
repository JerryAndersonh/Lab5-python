from chessPictures import SQUARE
from interpreter import draw
from picture import Picture

blanco = Picture(SQUARE)
negro = blanco.negative()

# Alternamos blanco y negro
fila = blanco.join(negro).horizontalRepeat(4)

draw(fila)
