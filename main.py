import random
import colorgram
from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
screen.colormode(255)
# Extracting the colors from the image
'''
colors = colorgram.extract('image.jpg', 10)

color_rgb = []
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    full_color = (r, g, b)
    color_rgb.append(full_color)

print(color_rgb)
'''
full_color=[ (231, 243, 237), (202, 159, 104), (231, 212, 105), (47, 103, 139), (133, 167, 191), (146, 80, 60), (198, 141, 162)]
# Get current window width and height
width = screen.window_width()
height = screen.window_height()
def get_the_position():
    tim.speed("fastest")
    tim.penup()
    tim.goto(-width/2,-height/2)
    tim.pendown()

tim.hideturtle()
get_the_position()

for z in range(10):
#set the sizing
    tim.penup()
    tim.goto(-width / 2, -height / 2 + 50 * z)
    tim.pendown()
    for i in range(10):
        tim.color(random.choice(full_color))
        tim.pendown()
        tim.dot(15)
        tim.penup()
        tim.forward(50)
screen.exitonclick()
