from re import T
from turtle import *
import keyboard
tr= True
def fl(t):
	t.fd(270)
	t.bk(540)
	t.fd(270)
def penud(t):
		
	t.penup()
	
	
	t.fd(180)
	t.lt(90)
	t.pendown()
def a (t):
	t.penup()
	t.lt(90)
	t.bk(180)
	t.lt(90)
	t.pendown()
def aa(t):
	t.lt(90)
	t.fd(540)
	t.bk(540)
	t.lt(90)
def pos(t,w,h):
	t.penup()
	t.goto(w,h)
	t.pendown()
def x(t):
	

		t.lt(45)
		t.fd(80)
		t.pensize(15)
		t.color("red")
		t.bk(160)
		t.fd(80)
		t.lt(90)
		t.fd(80)
		t.bk(160)
		
def o(t):
	t.penup()
	t.rt(90)
	t.fd(50)
	t.lt(90)
	t.color("green")
	t.pendown()
	for i in range(19):
		t.lt(20)
		t.fd(20)
		
		t.pensize(15)		
grid1 = Turtle()
grid1.hideturtle()
grid1.penup()                
grid1.goto(0, -50) 
grid1.showturtle() 
grid1.speed(9999999999999999999999999999)
grid1.penup()
grid1.left(90)
grid1.fd(320)
grid1.left(90)
grid1.pendown()
grid1.pensize(3)
fl(grid1)
grid1.penup()
grid1.lt(90)
grid1.fd(540)
grid1.lt(90)
grid1.pendown()
grid1.fd(270)
grid1.bk(540)
grid1.fd(270)
grid1.lt(90)
penud(grid1)
fl(grid1)
a(grid1)
fl(grid1)
a(grid1)
grid1.lt(90)
grid1.penup()
grid1.bk(360)
grid1.lt(90)
grid1.pendown()
grid1.fd(90)
grid1.lt(90)
grid1.bk(540)
grid1.lt(90)
grid1.fd(186)
grid1.rt(90)
grid1.hideturtle()
grid1.fd(540)
qq =0
ww = 0
ee=0
aa=0
ss=0
dd=0
zz=0
xx=0
cc=0
one=Turtle()
two=Turtle()
three= Turtle()
four=Turtle()
five=Turtle()
six=Turtle()
seven=Turtle()
eight=Turtle()
nine=Turtle()
def tf(i):
	i.hideturtle()
	i.speed('fastest')	
tf(one)
tf(two)
tf(three)		
tf(four)
tf(five)
tf(six)
tf(seven)
tf(eight)
tf(nine)
pos(one,-180,180)
pos(two,0,180)
pos(three,180,180)
pos(four,-180,0)
pos(five,0,0)
pos(six,180,0)
pos(seven,-180,-180)
pos(eight,0,-180)
pos(nine,180,-180)
s= 0
while s < 9:
	while tr:
		if keyboard.is_pressed('q')  and qq==0:
			print(x(one))
			tr = False
			s +=1
			qq+=1

		if keyboard.is_pressed('w') and ww==0:
			print(x(two))
			tr = False 
			s +=1
			ww +=1

		if keyboard.is_pressed('e') and ee==0:
			print(x(three))
			tr = False
			s +=1
			ee +=1

		if keyboard.is_pressed('a') and aa==0:
			print(x(four))
			tr = False
			s +=1
			aa +=1

		if keyboard.is_pressed('s') and ss==0:
			print(x(five))
			tr = False
			s +=1
			ss +=1

		if keyboard.is_pressed('d') and dd==0:
			print(x(six))
			tr = False
			s +=1
			dd +=1

		if keyboard.is_pressed('z') and zz==0:
			print(x(seven))
			tr = False
			s +=1
			zz +=1

		if keyboard.is_pressed('x') and xx==0:
			print(x(eight))
			tr = False
			s +=1
			xx +=1
		if keyboard.is_pressed('c') and cc==0:
			print(x(nine))
			tr = False
			s +=1
			cc +=1
	while tr==False:
		if keyboard.is_pressed('q') and qq==0:
			print(o(one))
			tr = True
			s +=1
			qq +=1

		if keyboard.is_pressed('w') and ww==0:
			print(o(two))
			tr = True
			s +=1
			ww+=1

		if keyboard.is_pressed('e') and ee==0:
			print(o(three))
			tr = True 
			s +=1
			ee+=1

		if keyboard.is_pressed('a') and aa==0:
			print(o(four))
			tr = True
			s +=1
			aa+=1

		if keyboard.is_pressed('s') and ss==0:
			print(o(five))
			tr = True
			s +=1
			ss+=1

		if keyboard.is_pressed('d') and dd==0:
			print(o(six))
			tr = True
			s +=1
			dd+=1

		if keyboard.is_pressed('z') and zz==0:
			print(o(seven))
			tr = True
			s +=1
			zz+=1

		if keyboard.is_pressed('x') and xx==0:
			print(o(eight))
			tr = True
			s +=1
			xx+=1
		if keyboard.is_pressed('c') and cc==0:
			print(o(nine))
			tr = True
			s +=1
			cc+=1
done()