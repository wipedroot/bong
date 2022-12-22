# Bong - A Simple Pong Clone in Python 

import turtle
import os # uncomment for sound on Linux
# import winsound # uncomment for sound on Windows

wind = turtle.Screen()
wind.title("Bong - A simple Pong clone, made with Python")
wind.bgcolor("black")
wind.setup(width=1000, height=600)
wind.tracer(0)

# Left side Spliff 

splf_l = turtle.Turtle()
splf_l.speed(0) # set animation speed
splf_l.shape("square") # set shape, default square is 20x20px
splf_l.color("green") # set colour
splf_l.shapesize(stretch_wid=5, stretch_len=1) # stretch to fit
splf_l.penup() # set pen state
splf_l.goto(-420, 0) # draw square 80px away from border 

# Right side Spliff 

splf_r = turtle.Turtle()
splf_r.speed(0)
splf_r.shape("square")
splf_r.color("red")
splf_r.shapesize(stretch_wid=5, stretch_len=1)
splf_r.penup()
splf_r.goto(420, 0)

# create the Bong

bong = turtle.Turtle()
bong.speed(0)
bong.shape("circle")
bong.color("white")
bong.penup()
bong.goto(0, 0)
bong.dx = 0.09
bong.dy = 0.09

# Score counters

score_one = 0
score_two = 0

# Scoreboard

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Green: 0  Red: 0", align="center", font=("Courier", 24, "normal"))

# Spliffs Movement

def splf_l_up():
	y = splf_l.ycor()
	y += 15
	splf_l.sety(y)

def splf_l_dwn():
	y = splf_l.ycor()
	y -= 15
	splf_l.sety(y)

def splf_r_up():
	y = splf_r.ycor()
	y += 15
	splf_r.sety(y)

def splf_r_dwn():
	y = splf_r.ycor()
	y -= 15
	splf_r.sety(y)

wind.listen()
wind.onkeypress(splf_l_up, "w")
wind.onkeypress(splf_l_dwn, "s")
wind.onkeypress(splf_r_up, "Up")
wind.onkeypress(splf_r_dwn, "Down")

# game loop 

while True:
	wind.update()

	# bong flying
	bong.setx(bong.xcor() + bong.dx)
	bong.sety(bong.ycor() + bong.dy)

#	game arena

	if bong.ycor() > 290:
		bong.sety(290)
		bong.dy *= -1
		os.system("aplay bong_bounce.wav&")
		#winsound.Playsound("bong_bounce.wav, winsound.SND_ASYNC") # uncomment for sound on Windows

	if bong.ycor() < -290:
		bong.sety(-290)
		bong.dy *= -1
		os.system("aplay bong_bounce.wav&")
		#winsound.Playsound("bong_bounce.wav, winsound.SND_ASYNC") # uncomment for sound on Windows

	if bong.xcor() > 490:
		bong.goto(0, 0)
		bong.dx *= -1
		score_one +=1
		score.clear()
		score.write("Green: {}  Red: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

	if bong.xcor() < -490:
		bong.goto(0, 0)
		bong.dx *= -1
		score_two +=1
		score.clear()
		score.write("Green: {}  Red: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

#   Swings

	if bong.xcor() > 410 and bong.xcor() < 420 and (bong.ycor() < splf_r.ycor() + 20 and bong.ycor() > splf_r.ycor() - 20):
		bong.setx(340)
		bong.dx *= -1
		os.system("aplay bong_bounce.wav&")
		#winsound.Playsound("bong_bounce.wav, winsound.SND_ASYNC") # uncomment for sound on Windows

	if bong.xcor() < -410 and bong.xcor() > -420 and (bong.ycor() < splf_l.ycor() + 20 and bong.ycor() > splf_l.ycor() - 20):
		bong.setx(-340)
		bong.dx *= -1
		os.system("aplay bong_bounce.wav&")
		#winsound.Playsound("bong_bounce.wav, winsound.SND_ASYNC") # uncomment for sound on Windows

