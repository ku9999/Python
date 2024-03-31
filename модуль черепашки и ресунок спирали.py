import turtle
n=int(input('введите плотность ресунка 2высокая ,5 низкая: '))
m=int(input('введите продолжительность сек 1=20 знач : '))
 
turtlePen = turtle.Turtle()
window = turtle.Screen()
 
 
def polygon(n, size=80):
    if n > 2:
        angle = 360/n
 
        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)
 
 
turtlePen.speed(10)
 
for i in range(0, m, n):
    polygon(3, 10 + i)
    turtlePen.left(20)
 
window.mainloop()
turtle.speed(10000)
