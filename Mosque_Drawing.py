import turtle
import time
t=turtle.Turtle()
def asd():
    time.sleep(3)
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()    
t.speed(100)
t.penup()
t.goto(-100,80)
t.pendown()
t.color("brown")
text="SABİLAL MUHTADİN MOSQUE \n(INDONASİA)"
t.begin_fill()
for i in range(2):
    t.fd(300)
    t.right(90)
    t.fd(70)
    t.right(90)
def mini():
    for i in range(2):
        t.begin_fill()
        t.fd(100)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.end_fill()
def don():
    t.left(90)
    t.penup()
    t.fd(35)
    t.pendown()
    t.right(90)
t.end_fill()
t.right(90)
t.penup()
t.fd(80)
t.pendown()
t.penup()
mini()
don()
t.pendown()
for i in range(9):
    mini()
    don()
t.penup()
t.fd(100)
t.right(90)
t.fd(400)
t.left(90)
t.pendown()
t.color("black")
t.begin_fill()
for i in range(2):
    t.fd(10)
    t.left(90)
    t.fd(400)
    t.left(90)
t.end_fill()
t.left(180)
t.penup()
t.fd(150)
t.right(90)
t.fd(300)
t.left(90)
t.pendown()
t.begin_fill()
t.circle(100,180)
t.left(90)
t.fd(200)
t.end_fill()
t.backward(100)
t.left(90)
t.fd(200)
t.left(90)
t.penup()
t.fd(200)
t.pendown()
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.right(90)
    t.backward(350)
    t.right(90)
t.end_fill()
t.penup()
t.backward(400)
t.pendown()
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.right(90)
    t.backward(350)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-180, -150)  
t.pendown()
t.fillcolor("blue")  
t.begin_fill()
t.right(60)  
t.backward(500)  
t.right(120)  
t.right(120) 
t.backward(500) 
t.end_fill()
t.penup()
t.penup()
t.goto(200,300)
t.pendown()
t.write(text, align="left", font=("Arial", 20, "bold"))
t.penup()
t.goto(-250,200)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.right(90)
    t.fd(200)
    t.right(90)
t.end_fill()
t.color("black")
for i in range(2):
    t.fd(40)
    t.right(90)
    t.fd(400)
    t.right(90)
    t.color("grey")
asd()
t.left(90)
t.speed(50)
text="NEGARA MOSQUE \n (MALASİA) \n Capacity=15.000 people"
def a():
    t.begin_fill()
def b():
    t.end_fill()
def c():
    t.penup()
def d():
    t.pendown()
a()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
b()
t.left(90)
t.fd(100)
t.right(90)
t.fd(150)
t.color("blue")
a()
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
b()
c()
t.backward(150)
t.right(90)
t.fd(50)
d()
a()
for i in range(2):
    t.fd(30)
    t.right(90)
    t.fd(350)
    t.right(90)
b()
t.right(90)
t.fd(350)
t.color("lightblue")
a()
t.circle(100)
b()
t.left(90)
t.fd(100)
t.color("black")
t.right(180)
for i in range(8):
    t.fd(100)
    t.backward(100)
    t.left(45)
t.right(90)
c()
t.fd(900)
t.left(90)
d()
t.color("lightblue")
a()
for i in range(2):
    t.fd(350)
    t.left(90)
    t.fd(30)
    t.left(90)
b()
t.color("red")
c()
t.fd(350)
t.left(90)
t.fd(15)
t.right(90)
d()
t.fd(70)
a()
t.circle(10)
b()
t.color("white")
a()
t.circle(7)
b()
t.color("red")
c()
t.goto(-300,300)
d()
t.write(text, align="left", font=("Arial", 20, "bold"))
c()
t.fd(2000)
d()
asd()
text="DJAMAA EL DJAZİR \n MOSQUE \n (ALGERİA) \n Capacity:120.000 "
t=turtle.Turtle()
turtle.bgcolor("brown")
t.speed(20)
t.color("grey")
t.begin_fill()
for q in range(2):
    t.fd(200)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.left(180)
t.penup()
t.fd(40)
t.pendown()
t.begin_fill()
for q in range(2):
    t.fd(200)
    t.right(90)
    t.fd(100)
    t.right(90)
t.end_fill()
t.penup()
t.fd(250)
t.pendown()
t.begin_fill()
for q in range(2):
    t.fd(200)
    t.right(90)
    t.fd(100)
    t.right(90)
t.end_fill()
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)
t.right(90)
t.color("black")
t.begin_fill()
t.circle(50,180)
t.end_fill()
t.left(90)
t.penup()
t.fd(800)
t.pendown()
t.color("lightblue")
t.begin_fill()
for i in range(2):
    t.fd(50)
    t.right(90)
    t.fd(-200)
    t.right(90)
t.end_fill()
t.left(90)
t.fd(200)
t.right(90)
t.fd(25)
t.color("darkblue")
t.begin_fill()
t.circle(10)
t.end_fill()
t.color("brown")
t.begin_fill()
t.circle(7)
t.end_fill()
t.penup()
t.color("black")
t.goto(400,200)
t.pendown()
t.write(text, align="left", font=("Arial", 20, "bold"))
t.penup()
t.fd(500)
t.pendown()
asd()
turtle.bgcolor("light grey")
t.color("sandybrown")
def a():
    t.begin_fill()
def b():
    t.end_fill()
def c():
    t.penup()
def d():
    t.pendown()
text="HAGİA SOPHİA MOSQUE \n (TURKEY)"
c()
t.goto(-350,-350)
d()
a()
for i in range(4):
    t.fd(500)
    t.left(90)
b()
t.left(180)
t.color("brown")
a()
for i in range(2):
    t.fd(100)
    t.right(90)
    t.fd(700)
    t.right(90)
b()
c()
t.left(180)
t.fd(500)
d()
a()
for i in range(2):
    t.backward(100)
    t.right(90)
    t.backward(700)
    t.right(90)
b()
c()
t.left(180)
t.fd(200)
t.right(90)
t.fd(500)
d()
t.color("black")
a()
t.right(90)
t.fd(100)
t.left(90)
t.circle(100,90)
b()
t.left(90)
t.fd(100)
t.right(90)
c()
t.fd(200)
d()
a()
t.right(90)
t.fd(100)
t.left(90)
t.circle(100,90)
b()
t.left(90)
t.fd(100)
a()
t.color("grey")
t.right(90)
t.circle(100,-180)
t.left(90)
t.fd(200)
b()
c()
t.goto(400,300)
d()
t.color("red")
t.write(text, align="left", font=("Arial", 20, "bold"))
asd()
t.left(180)
t.speed(10)
t.fillcolor("yellow")
turtle.bgcolor("lightblue")
t.color("red")
t.begin_fill()
text="NİGARİA ABUJA MOSQUE"
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()
t.color("yellow")
t.begin_fill()
for q in range(2):
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(30)
t.end_fill()
t.left(90)
t.forward(150)
t.color("green")
t.begin_fill()
t.circle(-75,180)
t.end_fill()
t.penup()
t.fd(150)
t.pendown()
t.color("yellow")
t.begin_fill()
for q in range(2):
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(200)
t.end_fill()
t.penup()
t.left(270)
t.fd(105)
t.right(90)
t.fd(225)
t.pendown()
t.fd(40)
t.begin_fill()
t.color("green")
t.circle(10)
t.end_fill()
t.begin_fill()
t.color("lightblue")
t.circle(7)
t.end_fill()
t.color("green")
t.right(180)
t.fd(40)
t.fd(50)
t.backward(50)
t.penup()
t.goto(-300,200)
t.pendown()
t.write(text, align="left", font=("Arial", 20, "bold"))
asd()
text="HASSAN 2 MOSQUE \n (MOROCCO) \n Capacity: 105.000 peoples"
t=turtle.Turtle()
t.speed(50)
turtle.bgcolor("grey")
t.color("sandybrown")
t.begin_fill()
t.fd(400)
t.left(90)
t.fd(100)
t.left(90)
t.fd(50)
t.right(90)
t.fd(100)
t.left(90)
t.fd(300)
t.left(90)
t.fd(100)
t.right(90)
t.fd(50)
t.left(90)
t.fd(100)
t.end_fill()
t.right(90)
t.backward(150)
t.right(90)
t.fd(200)
t.begin_fill()
for i in range(2):
    t.fd(50)
    t.right(90)
    t.fd(100)
    t.right(90)
t.end_fill()
t.left(180)
t.fd(150)
t.color("brown")
t.left(90)
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.fd(30)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.fd(30)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.fd(30)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.fd(30)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.fd(30)
t.pendown()
t.penup()
t.fd(300)
t.pendown()
t.begin_fill()
for i in range(2):
    t.fd(70)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()
t.fd(20)
t.color("lightblue")
t.begin_fill()
for i in range(2):
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()
t.left(90)
t.fd(300)
t.fd(30)
t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()
t.color("grey")
t.begin_fill()
t.circle(7)
t.end_fill()
t.right(-180)
t.penup()
t.fd(400)
t.pendown()
t.color("black")
t.begin_fill()
for i in range(2):
    t.fd(20)
    t.right(90)
    t.fd(600)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-400,250)
t.pendown()
t.color("green")
t.write(text, align="left", font=("Arial", 20, "bold"))
t.penup()
t.fd(2000)
asd()
t=turtle.Turtle()
text="FASİAL MOSQUE (PAKİSTAN) CAPACTİY:300.000 PEOPLES"
t.speed(10)
turtle.bgcolor("black")
t.color("grey")
def a():
    t.begin_fill()
def b():
    t.end_fill()
def c():
    t.penup()
def d():
    t.pendown()
def town():
    a()
    for i in range(2):
        t.fd(50)
        t.left(90)
        t.fd(300)
        t.left(90)
    b()
    a()
    t.left(90)
    t.fd(300)
    t.fd(90)
    t.right(135)
    t.fd(110)
    b()
t.color("light gray")
a()
for _ in range(5):
    t.forward(200)
    t.left(72)
b()
t.color("dark gray")
a()
for i in range(3):
    t.fd(200)
    t.left(120)
b()
town()
c()
t.left(45)
t.goto(200,0)
d()
town()
c()
t.goto(-200,-200)
d()
t.color("yellow")
t.write(text, align="left", font=("Arial", 20, "bold"))
c()
t.fd(1000)
d()
asd()
t=turtle.Turtle()
text="the mosque on the left, the qibla masjid, \n the mosque on the right, the Kubbetus Sahra mosque the black line is the burak wall \n Mescidi Aksa(PALASTİNE) Capacity:400.000 peoples"
t.speed(50)
t.color("black")
t.penup()
t.left(90)
t.fd(200)
t.left(90)
t.fd(200)
t.left(180)
t.pendown()
t.begin_fill()
for i in range(2):
    t.fd(750)
    t.right(90)
    t.fd(400)
    t.right(90)
t.end_fill()
t.right(90)
t.fd(30)
t.left(90)
t.penup()
t.fd(30)
t.pendown()
t.color("green")
t.begin_fill()
for i in range(2):
    t.fd(660)
    t.right(90)
    t.fd(340)
    t.right(90)
t.end_fill()
t.penup()
t.goto(200,0)
t.pendown()
def uma():
    t.color("lightblue")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(100)
        t.left(90)
    t.end_fill()
    t.left(90)
    t.fd(100)
    t.right(90)
    t.fd(150)
    t.color("yellow")
    t.left(90)
    t.begin_fill()
    t.circle(50,180)
    t.end_fill()
def qibla():
    t.color("sandybrown")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(100)
        t.left(90)
    t.end_fill()
    t.fd(200)
    t.color("brown")
    t.left(90)
    t.begin_fill()
    t.circle(50,-180)
    t.end_fill()
uma()
t.right(90)
t.penup()
t.fd(200)
t.pendown()
qibla()
t.penup()
t.goto(-500,300)
t.pendown()
t.color("red")
t.write(text, align="left", font=("Arial", 15, "bold"))
asd()
t=turtle.Turtle()
text="KAABE(SAUDİ ARABİA) \n  الكعبة \n Capactiy:4.000.000 Peoples"
t.speed(100)
turtle.bgcolor("light grey")
t.penup()
t.goto(-100,-100)
t.pendown()
t.begin_fill()
for i in range(4):
    t.fd(300)
    t.left(90)
t.end_fill()
t.left(90)
t.fd(200)
t.color("yellow")
t.begin_fill()
for i in range(2):
    t.fd(10)
    t.right(90)
    t.fd(300)
    t.right(90)
t.end_fill()
t.penup()
t.goto(100,-100)
t.pendown()
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()
t.color("black")
t.penup()
t.goto(300,200)
t.pendown()
t.color("red")
t.write(text, align="left", font=("Arial", 20, "bold"))
t.penup()
t.fd(900)
asd()
t.color("green")
turtle.bgcolor("light grey")
text="المسجد النبوي \n Al-Masjid an-Nabawi(Saudia Arabia) \n Capatiy:1.500.000 peoples"
t.speed(100)
t.begin_fill()
t.circle(100,180)
t.end_fill()
t.left(180)
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(30)
    t.left(90)
t.penup()
t.goto(200,200)
t.pendown()
t.color("blue")
t.write(text, align="left", font=("Arial", 20, "bold"))
t.penup()
t.fd(1000)
asd()
turtle.bgcolor("black")
turtle.done()
###Mosque_Drawing_2###

