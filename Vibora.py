# Juego de la Víbora basado en la colección de FreeGames
# donde se hicieron modificaciones para una mejor experiencia
# de juego.
# Autores: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Fecha: 23/03/2023

# Se importan las librerías que se utilizarán.
from turtle import *
from random import randrange, choice
from freegames import square, vector

# Se establecen los cinco colores diferentes para colorear
# a la serpiente y la comida, sin incluir el rojo.
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar colores aleatorios a la serpiente y la comida
snake_color = choice([c for c in colors if c != 'red'])
colors.remove(snake_color)
food_color = choice([c for c in colors if c != 'red'])
colors.remove(food_color)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(20, -20)

# Función que cambia la dirección de la serpiente.
# Toma como parámetro las coordenadas x y y a las que
# se moverá la serpiente.
# No hay valor de retorno.
def change(x, y):
    aim.x = x
    aim.y = y

# Función que evalúa si la cabeza está dentro de los
# límites.
# Toma como parámetro la cabeza.
# Regresa Verdadero si la cabeza está dentro de los 
# límites. En caso contrario regresa Falso.
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Función que mueve a la serpiente hacia delante por
# un segmento.
# No toma parámetros.
# Regresa un return vacío si la cabeza está no está
# dentro de los límites o si la cabeza está en la
# serpiente para romper la función.
def move():
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
        # Se guarda ahora el color actualizado de la serpiente.
        square(body.x, body.y, 9, snake_color)

    # Se guarda ahora el color actualizado de la comida.
    square(food.x, food.y, 9, food_color)
    update()

    # Actualizar la posición de la comida aleatoriamente
    if randrange(10) == 0:
        food.x += 10
        if food.x < -200:
            food.x = -190
        elif food.x > 190:
            food.x = 180
    elif randrange (10) == 1:
        food.y += 10
        if food.y < -200:
            food.y = -190
        elif food.y > 190:
            food.y = 180

    ontimer(move, 200)

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