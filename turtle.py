from turtle import *
import colorsys

speed(5)
pensize(2)
bgcolor("black")

hue = 0.0

for i in range(150):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    hue += 0.008

    rt(i)
    circle(200, i)
    fd(i)
    rt(90)

done()
