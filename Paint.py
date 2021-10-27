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
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    r = (end.x - start.x)/2
    circle(r)
    end_fill()  # TODO


def triangle(start, end):

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



def triangle(start, end):

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

def info_alumnos():
    writer.up()
    writer.goto(0, 190)
    writer.color('red')
    writer.write("Samuel Acosta")
    writer.goto(0, 170)
    writer.color('red')
    writer.write("Ricardo Olmedo")


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
writer = Turtle(visible=False)
#onkey necesita una fx sin argumentos por eso se uso la lambda - funcion anonima sin argumentos
#los colores pueden usarse hexadecimales que los obtenemos de internet
info_alumnos()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('B350FF'), 'P') # P de purple porque el color es morado
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

#onkey(lambda: store('shape', info_alumnos), 'a')
done()
