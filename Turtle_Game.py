# Import relevant modules
import turtle
import random
import time
# Setting the screen for the game
screen = turtle.Screen()

screen.bgcolor('lightblue')

# We want two players
player_one= turtle.Turtle()
player_one.color('red')
player_one.shape('turtle')

player_two= player_one.clone()
player_two.color('blue')

# Let's position the players
player_one.penup()
player_one.goto(-500, 200)

player_two.penup()
player_two.goto(-500, -200)

# Let's draw a finish line

player_one.goto(400, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=100)

#Allows player one to return to his starting position

player_one.penup()
player_one.color('red')
player_one.goto(-500, 200)
player_one.right(90)

# make both players have pens down

player_one.pendown()
player_two.pendown()

# Create value for a die

die= [1, 2, 3, 4, 5, 6]

for i in range(30):
    if player_one.pos() >= (400, 300):
        print('Player one wins the game!')
        break
    elif player_two.pos() >= (400, -300):
        print('Player two wins the game!')
        break
    else:
        die_roll= random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2= random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(1)

# Keeps the turtle drawing on the screen
turtle.done()