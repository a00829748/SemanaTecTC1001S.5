"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#lista de colores que puede tomar snake y la comida
colores = ['green','orange','yellow','blue','purple','#00FFF3','#000000','#FFFFFF','pink','grey','#003300','cyan']
#Se elige el color para el snake
snake_color = choice(colores)
#Se quita la opcion de color para no repetir
colores.remove(snake_color)
#Elegir el color de la comida
food_color = choice(colores)
#Remover el color en uso
colores.remove(food_color)
#agregar el color de backround
bgcolor(choice(colores))

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color) #se diversifica el color del snake

    square(food.x, food.y, 9, food_color) #se diversifica el color del food
    update()
    ontimer(move, 100)

def info_alumnos():
    writer.up()
    writer.goto(0, 190)
    writer.color('red')
    writer.write("Samuel Acosta")
    writer.goto(0, 170)
    writer.color('red')
    writer.write("Ricardo Olmedo")

writer = Turtle(visible=False)
info_alumnos()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
