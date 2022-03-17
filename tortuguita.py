import argparse
from time import sleep

import turtle

parser = argparse.ArgumentParser(description='Simple script to draw FAESA\'s logo.')

parser.add_argument('-x', '--x_coord', type=int, default=0, help='X coordinate is set to 0 by default.')
parser.add_argument('-y', '--y_coord', type=int, default=0, help='Y coordinate is set to 0 by default.')
parser.add_argument('--sleep', action='store_true', help='Sleep 10 seconds before close the window.')

args = parser.parse_args()

x = args.x_coord
y = args.y_coord

INNER_SQUARE_LENGTH = 106
SQUARE_SIDE = 150
FIRST_ANGLE = 90
SECOND_ANGLE = 45
SLEEP_TIME = 10

turtle.Turtle()
turtle.speed(2)

def prepare_to_draw(x, y):
    '''Prepare the pen for a new draw'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# draws the first square
prepare_to_draw(x, y)

for i in range(4):
    turtle.forward(SQUARE_SIDE)
    turtle.left(FIRST_ANGLE)

half_sq_side = SQUARE_SIDE / 2

# draws the second square
prepare_to_draw(x + half_sq_side, y)

degrees = SECOND_ANGLE

for i in range(4):
    turtle.left(degrees)
    turtle.forward(INNER_SQUARE_LENGTH)

    degrees = FIRST_ANGLE

# resets
turtle.left(SECOND_ANGLE)
degrees = SECOND_ANGLE

# details from the second square
portion = INNER_SQUARE_LENGTH / 3
control = portion

for i in range(8):
    turtle.left(degrees)
    turtle.forward(control)

    degrees = FIRST_ANGLE

    if i == 0:
        control = portion * 2

    if i in [1, 2, 3, 4, 5]:
        control = portion
        degrees = -FIRST_ANGLE

    if i == 6:
        degrees = FIRST_ANGLE
        control = portion

# returns to 0,0 position
turtle.penup()
turtle.home()

if args.sleep:
    sleep(args.sleep)

    print(SLEEP_TIME)