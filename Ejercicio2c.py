from chessPictures import QUEEN
from interpreter import draw
from picture import Picture

queen = Picture(QUEEN)
fila_reinas = queen.horizontalRepeat(4)

draw(fila_reinas)
