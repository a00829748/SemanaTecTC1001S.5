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
    #sube el lapiz
    up()
    goto(start.x, start.y)
    #baja el lapiz para dibujar
    down()
    #inicial el filla - para rellenar
    begin_fill()
    
    #se ejecutara 4 veces
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle2(start, end):
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

    # Si es el primer click sobre la window
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


#indica lo que va a dibujar - a funcion que se va a ejecutar
#shape indica lo que se va a dibujar
#'start' - vector del primer click -o None -  si ya se usaron 2 clicks
state = {'start': None, 'shape': line}
print(type(state))
#Inicializar la ventana con ancho, alto y posicion x,y
#sets up windows to 420x200 pixels, in upper left of screen
#none y none te lo centra
setup(width=420, height=420, startx=0, starty=0)
onscreenclick(tap)
listen()
#onkey necesita una fx sin argumentos por eso se uso la lambda - funcion anonima sin argumentos
#los colores pueden usarse hexadecimales que los obtenemos de internet
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('B350FF'), 'P') # P de purple ya que el nuevo color sera morado
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()