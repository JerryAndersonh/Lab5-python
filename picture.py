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

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados en sentido horario"""
    if not self.img:
        return Picture([])
    rotated_img = []
    for col in range(len(self.img[0])):
        new_row = ''.join([row[col] for row in self.img])[::-1]
        rotated_img.append(new_row)
    return Picture(rotated_img)