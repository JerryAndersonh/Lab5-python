# 🧠 Tarea: Dibujar un Tablero de Ajedrez en Python

## 📌 Descripción General

Esta tarea tuvo como objetivo aplicar los conocimientos adquiridos en programación con Python para desarrollar un tablero de ajedrez utilizando una estructura basada en listas de cadenas de texto (strings). Si bien la parte gráfica ya estaba desarrollada, el enfoque de la tarea se centró en la implementación de estructuras de datos y métodos para manipular imágenes representadas por caracteres de texto.

---

## ⚙️ Preparación del Entorno

Para el correcto desarrollo de la tarea, se realizó la configuración de un entorno virtual llamado `venv` con el siguiente procedimiento:

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

Luego, se instaló la biblioteca gráfica `pygame` requerida para visualizar las figuras:

```bash
pip install pygame
```

Este entorno permitió mantener el proyecto organizado y aislado de otras configuraciones del sistema.

---

## 🧩 Objetivos de la Tarea

* Implementar métodos que manipulen imágenes de piezas de ajedrez representadas como listas de strings.
* Utilizar herramientas básicas de Python como comprensión de listas, `map`, `zip`, `range`, operaciones con strings y estructuras de control.
* Componer imágenes complejas (como el tablero de ajedrez completo) a partir de piezas más simples.
* Aplicar buenas prácticas de programación modular y reutilización de código.
* Controlar el avance del proyecto mediante Git y registrar cambios en GitHub.

---

## 📁 Archivos y Recursos Utilizados

* `pieces.py`: Contiene la clase `Picture` y las representaciones en caracteres de las piezas de ajedrez.
* `colors.py`: Contiene el mapeo de colores y su inverso usado para generar imágenes negativas.
* `chessPictures`: Módulo que proporciona objetos `Picture` como `rock`, `knight`, `bishop`, `queen`, `king` y `square`.
* `interpreter.py`: Permite visualizar las figuras con el método `draw()`.

---

## 🧪 Métodos Implementados en la Clase `Picture`

Se implementaron los siguientes métodos en la clase `Picture`, los cuales operan sobre el atributo `img`, que es una lista de strings:

### `verticalMirror()`

Devuelve la imagen reflejada verticalmente. Cada línea se invierte utilizando slicing.

### `horizontalMirror()`

Devuelve la imagen reflejada horizontalmente. Se invierte el orden de las líneas.

### `negative()`

Devuelve la imagen con colores invertidos. Utiliza el mapeo definido en `colors.py` para transformar cada carácter.

### `join(picture)`

Concatena horizontalmente la imagen actual con otra imagen recibida como argumento.

### `up(picture)`

Pone la imagen recibida como argumento encima de la imagen actual, concatenando ambas verticalmente.

### `under(picture)`

Superpone una imagen sobre otra. Si la imagen de encima tiene un carácter distinto a espacio (`' '`), ese carácter prevalece.

### `horizontalRepeat(n)`

Repite la imagen actual horizontalmente `n` veces.

### `verticalRepeat(n)`

Repite la imagen actual verticalmente `n` veces.

---

## 💻 Código Fuente (Ejemplo)

```python
class Picture:
    def __init__(self, img):
        self.img = img

    def verticalMirror(self):
        return Picture([line[::-1] for line in self.img])

    def horizontalMirror(self):
        return Picture(self.img[::-1])

    def negative(self):
        from colors import _invColor
        return Picture([
            ''.join([_invColor(c) for c in line])
            for line in self.img
        ])

    def join(self, p):
        return Picture([
            l1 + l2
            for l1, l2 in zip(self.img, p.img)
        ])

    def up(self, p):
        return Picture(p.img + self.img)

    def under(self, p):
        return Picture([
            ''.join([c2 if c2 != ' ' else c1 for c1, c2 in zip(l1, l2)])
            for l1, l2 in zip(self.img, p.img)
        ])

    def horizontalRepeat(self, n):
        return Picture([line * n for line in self.img])

    def verticalRepeat(self, n):
        return Picture(self.img * n)
```

---

## 🌟 Resultados

Después de implementar y probar cada método de forma individual, se utilizaron para construir composiciones más complejas, incluyendo:

* Cuadrados alternados blanco/negro.
* Filas con peones y otras piezas.
* Tablero completo de ajedrez 8x8 con piezas ubicadas en sus posiciones iniciales.

Estas figuras se visualizaron utilizando:

```python
from interpreter import draw
from chessPictures import *
draw(rock.horizontalMirror())
```

---

## 🔧 Repositorio y Control de Versiones

Este proyecto fue gestionado con Git, permitiendo el seguimiento detallado de los cambios mediante *commits*. Puedes acceder al repositorio en GitHub desde el siguiente enlace:

🔗 [Repositorio GitHub - Tarea del Ajedrez](https://github.com/rescobedoq/pw2/tree/main/labs/lab04/Tarea-del-Ajedrez)

---

## 📸 Evidencia de Commits

A continuación, se muestra una imagen con el historial de *commits* realizados durante el desarrollo:

![Evidencia de Commits](ruta/a/la/imagen.png)

> Reemplaza `ruta/a/la/imagen.png` por la ubicación de tu imagen de commits dentro del repositorio (puede ser `assets/commits.png` por ejemplo).

---

## ✅ Conclusión

Esta tarea representó una excelente oportunidad para consolidar conceptos fundamentales de Python, especialmente en el trabajo con listas, comprensión de listas y manipulación de strings. Además, permitió ejercitar la creatividad al componer imágenes y reforzar el uso de Git como herramienta de control de versiones.

El resultado fue la construcción modular de un tablero de ajedrez completamente funcional desde cero, aplicando exclusivamente métodos definidos por el estudiante. El uso de estructuras simples demostró ser suficiente para lograr un objetivo visual interesante y educativo.

---

🗓️ *Trabajo realizado por \[Tu Nombre Aquí], para el curso de Programación Web II.*
