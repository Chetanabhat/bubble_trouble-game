import turtle
import os
import math
import random

#set up screen

wn=turtle.Screen()
wn.bgcolor("black")         #change the background color 
wn.title("bubble trouble")


#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score=0

#draw the score
score_pen =turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="score:%s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()


#create the player turtle
player=turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspeed = 15


#choose the no of enimies
no_of_enemies = 5
no_of_enemies1=5
no_of_enemies2=5
#create an empty list
enemies=[]
enem=[]
ene=[]

#add enimies to the list
for i in range(no_of_enemies):
    #create enimies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed=3

#add  green enimies to the list
for i in range(no_of_enemies1):
    #create enimies
    enem.append(turtle.Turtle())

for e in enem:
    e.color("green")
    e.shape("circle")
    e.penup()
    e.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    e.setposition(x,y)

espeed=3

#add  blue enimies to the list
for i in range(no_of_enemies2):
    #create enimies
    ene.append(turtle.Turtle())

for ee in ene:
    ee.color("blue")
    ee.shape("circle")
    ee.penup()
    ee.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    ee.setposition(x,y)

eespeed=3

#create players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 25

#define bullet state
bulletstate = "ready"

#move the player left to right
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x < -280:
        x= -280
    player.setx(x)


def move_right():
    x=player.xcor()
    x+=playerspeed
    if x > 280:
        x= 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate =="ready":
        bulletstate = "fire"
        #move the bullet to jump above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()

def iscollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#main game loop
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)
        #move the enemy back and down
        if enemy.xcor()> 280:
            #move all the enemies down
            for e in enemies:
                y=e.ycor()
                y -=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1
            
        if enemy.xcor() <-280:
            #move all the enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1

        #check for the collision between the bullet and the enemy
        if iscollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score-=10
            scorestring="score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        #collision with enemy and player
        if iscollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    for enemy in enem:
        x=enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)
        #move the enemy back and down
        if enemy.xcor()> 280:
            #move all the enemies down
            for e in enem:
                y=e.ycor()
                y -=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1
            
        if enemy.xcor() <-280:
            #move all the enemies down
            for e in enem:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1    

    



            

        #check for the collision between the bullet and the enemy
        if iscollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score+=10
            scorestring="score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        #collision with enemy and player
        if iscollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    for enemy in ene:
        x=enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)
        #move the enemy back and down
        if enemy.xcor()> 280:
            #move all the enemies down
            for e in ene:
                y=e.ycor()
                y -=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1
            
        if enemy.xcor() <-280:
            #move all the enemies down
            for e in ene:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1    

    



            

        #check for the collision between the bullet and the enemy
        if iscollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score+=20
            scorestring="score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        #collision with enemy and player
        if iscollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break


        


    #move bullet
    if bulletstate=="fire":
        y = bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
    
