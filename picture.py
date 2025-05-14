from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    inverted_img = [''.join([self._invColor(c) for c in row]) for row in self.img]
    return Picture(inverted_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    joined_img = [s_row + p_row for s_row, p_row in zip(self.img, p.img)]
    return Picture(joined_img)

  def up(self, p):
    return Picture(self.img + p.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    return Picture(p.img + self.img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado n veces """
    return Picture([row * n for row in self.img])

  def verticalRepeat(self, n):
    return Picture(self.img * n)
  
  def superponer(pieza, casilla):
    """Superpone la pieza sobre la casilla, asumiendo que tienen las mismas dimensiones."""
    filas_combinadas = []
    for fila_pieza, fila_casilla in zip(pieza.img, casilla.img):
        fila_combinada = []
        for p, c in zip(fila_pieza, fila_casilla):
            # Si el carácter de la pieza no es "transparente", usar ese
            fila_combinada.append(p if p != ' ' else c)
        filas_combinadas.append(''.join(fila_combinada))
    return Picture(filas_combinadas)