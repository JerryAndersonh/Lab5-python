from chessPictures import *
from interpreter import draw
from picture import Picture

# Casillas
blanco = Picture(SQUARE)
negro  = blanco.negative()

# Piezas blancas
torre_b   = Picture(ROCK)
caballo_b = Picture(KNIGHT)
alfil_b   = Picture(BISHOP)
reina_b   = Picture(QUEEN)
rey_b     = Picture(KING)
peon_b    = Picture(PAWN)

# Piezas negras
torre_n   = torre_b.negative()
caballo_n = caballo_b.negative()
alfil_n   = alfil_b.negative()
reina_n   = reina_b.negative()
rey_n     = rey_b.negative()
peon_n    = peon_b.negative()

def colocar_sobre_casillas(piezas, fila_clara_primero):
    fila = []
    for i, pieza in enumerate(piezas):
        casilla = blanco if (i + fila_clara_primero) % 2 == 0 else negro
        pieza_con_fondo = Picture.superponer(pieza, casilla)
        fila.append(pieza_con_fondo)
    
    resultado = fila[0]
    for p in fila[1:]:
        resultado = resultado.join(p)
    return resultado

def fila_vacia(fila_clara_primero):
    fila = []
    for i in range(8):
        casilla = blanco if (i + fila_clara_primero) % 2 == 0 else negro
        fila.append(casilla)
    resultado = fila[0]
    for c in fila[1:]:
        resultado = resultado.join(c)
    return resultado

# Fila 1: piezas blancas (casilla negra primero)
fila1 = colocar_sobre_casillas(
    [torre_b, caballo_b, alfil_b, reina_b, rey_b, alfil_b, caballo_b, torre_b],
    fila_clara_primero=1
)

# Fila 2: peones blancos (casilla blanca primero)
fila2 = colocar_sobre_casillas([peon_b]*8, fila_clara_primero=0)

# Filas 3–6: vacías, alternando color
fila3 = fila_vacia(fila_clara_primero=1)
fila4 = fila_vacia(fila_clara_primero=0)
fila5 = fila_vacia(fila_clara_primero=1)
fila6 = fila_vacia(fila_clara_primero=0)

# Fila 7: peones negros (casilla negra primero)
fila7 = colocar_sobre_casillas([peon_n]*8, fila_clara_primero=1)

# Fila 8: piezas negras (casilla blanca primero)
fila8 = colocar_sobre_casillas(
    [torre_n, caballo_n, alfil_n, reina_n, rey_n, alfil_n, caballo_n, torre_n],
    fila_clara_primero=0
)

# Tablero completo
tablero = (
    fila1
    .under(fila2)
    .under(fila3)
    .under(fila4)
    .under(fila5)
    .under(fila6)
    .under(fila7)
    .under(fila8)
)

draw(tablero)
