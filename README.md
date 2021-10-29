# Actividad2 - Paint.py
## Cosas que se realizaron
- Agregar codigo inicial y README inicial
- Agregar codigo para rectangulo
- Agregar codigo para triangulo
- Agragar codigo para color nuevo
- Agregar codigo para circulo
- Agregar codigo para mostrar integrantes
## Agregar el codigo inicial y README - Samuel Acosta 100
```Python
"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO


def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO


def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
```
## Completar el codigo para realizar un rectángulo - Samuel Acosta
```
def rectangle(start, end):
    "Draw rectangle from start to end."
    #sube el lapiz
    up()
    goto(start.x, start.y)
    #se baja el lapiz para dibujar
    down()
    #iniciar el fill pa/ rellenar
    begin_fill()
    
    #se ejecutara 2 veces
    for count in range(2):
    #se calcula la distancia en el eje de las x
        forward(end.x - start.x)
    #se voltea 90 grados
        left(90)
    #se calcula la distancia en el eje de las y
        forward(end.y - start.y)
    #Se vuelve a voltear 90 grados para cerrar.
        left(90)
    
    end_fill()
```
## Completar el codigo para realizar un triángulo - Samuel Acosta
```
def triangle(start, end):
    "Draw triangle from start to end."
    #sube el lapiz
    up()
    goto(start.x, start.y)
    #se baja el lapiz para dibujar
    down()
    #iniciar el fill para rellenar
    begin_fill()
    
    #se calcula la distancia entre cada vertice del triangulo
    forward(end.x - start.x)
    for count in range(2):
        #Gira para poder cerrar el triángulo
        left(120)
        #el tramo de vértice a vértice
        forward(end.x - start.x)
    
    end_fill()
```
## Completar el codigo para usar un color nuevo - Ricardo Olmedo
```
onkey(lambda: color('B350FF'), 'P') # P de purple porque el color es morado
```

## Completar el codigo para realizar un circulo - Ricardo Olmedo
```
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    r = (end.x - start.x)/2
    circle(r)
    end_fill()  # TODO
```
## Integrar el codigo para mostrar nombres de los integrantes - Ricardo Olmedo 100
```python
def info_alumnos():
    writer.up()
    writer.goto(0, 190)
    writer.color('red')
    writer.write("Samuel Acosta")
    writer.goto(0, 170)
    writer.color('red')
    writer.write("Ricardo Olmedo")
    
    
writer = Turtle(visible=False)
```
