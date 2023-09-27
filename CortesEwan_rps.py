# This file was created by: Ewan Cortes

# Import turtle and package, and accesss to the turtle library
import turtle
from turtle import *

# Import random, and access to the random library
import random
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd()) # These two will print the cwd and path directory in the terminal.
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# Setup the game and images folder in order to retrieve the images for the game
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# Setup the WIDTH and HEIGHT of the canvas as well declare the width and height of each images for later
WIDTH, HEIGHT = 1000, 600

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# Setup the screen class
screen = turtle.Screen()
screen.title("Rock, Paper, Scissors") # Create a name for the window

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

def rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y) 

# Set up a default font for easier access
font = font = ("Arial", 12, "normal")
# Setup the global computer and user score for the game
computer_count = 0
user_count = 0

# Setup the in between function for rerouting from onkeypressed to the userpicked() function.
def Rock():
    userpicked("rock") # For example, when the user presses "r" the function Rock() will play and set "user_choice" as "rock"
def Paper():
    userpicked("paper")
def Scissors():
    userpicked("scissors")

# Set up function for outcomes of choice
def userpicked(user_choice):
    # Make sure the function recognizes the global user and computer count variables
    global computer_count
    global user_count

    # Tell turtle to have its pen up so the user doesn't see it
    turtle.penup()

    # Set up the computer choice by creating a list of choices and using a random to select a random "choice" from the list(basechoice)
    basechoice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(basechoice)

    # Set the defaul color to white
    turtle.color('white')

    # Make sure this if statement only works if the game is still going (below 2 points for either user or computer)
    # This if statement will either write that the User won one round, that the computer won one round, or that it was tie.
    # If the user count = 2 then it will print that the user won the game and vice versa for the computer
    if computer_count != 2 or user_count != 2:
        if user_choice == computer_choice: # Setup the tie statement so that if computer choice = user choice nothing happens and no score is added
                turtle.clear()
                turtle.goto(0, 200)
                turtle.write(f"Both players selected {user_choice}. It's a tie!", align="center", font=font)
        
        # This elif statement is for when the use either wins one round or the game after displaying what the computer chose
        elif user_choice == "rock" and computer_choice == "scissors" or \
            user_choice == "scissors" and computer_choice == "paper" or \
            user_choice == "paper" and computer_choice == "rock":
            turtle.clear()
            user_count += 1 # Adds one point to the user count
            if user_count < 2: # Count is added before this in order to make sure game ends with looping
                turtle.goto(0,200)
                turtle.write(f"Computer chose {computer_choice}. You Win One Round!!!", False, align="center", font=font)
                turtle.hideturtle() # Hides turtle (same thing for rest in code)
            else: # For when the game ends
                turtle.goto(0, 200)
                turtle.color("red")
                turtle.write(f"Computer chose {computer_choice}. YOU WON THE GAAME!!! WOO!", False, align="center", font=("Times New Roman", 24, 'normal'))
                turtle.hideturtle()

        # This elif statement is for when the computer either wins one round or the game
        elif computer_choice == "rock" and user_choice == "scissors" or \
            computer_choice == "scissors" and user_choice == "paper" or \
            computer_choice == "paper" and user_choice == "rock":
            turtle.clear()
            computer_count += 1 # Adds one point to the user count
            if computer_count < 2: # Count is added before this in order to make sure game ends with looping
                turtle.goto(0,200)
                turtle.write(f"Computer chose {computer_choice}. You Lost One Round. :(", False, align="center", font=font)
                turtle.hideturtle()
            else: # For when the game ends
                turtle.goto(0, 200)
                turtle.color("red")
                turtle.write(f"Computer chose {computer_choice}. YOU LOST THE GAME! u suck :(", False, align="center", font=("Times New Roman", 24, 'normal'))
                turtle.hideturtle()

        # After all the if statements no matter what this message will show and ask the user to play another round
        turtle.goto(0, -200)
        turtle.color("red")
        turtle.write("Click Play[B] to play again!", False, align='center', font=("Times New Roman", 24, 'bold'))
        turtle.hideturtle()
    # If the user wants to play again this onkeypress command will tell turtle to go to the play function from the press of "b"
    screen.onkeypress(play, 'b')
    

# This is the primary function of the game and everything runs from this
def play():
    # Make sure the function recognizes the global user and computer count variables
    global computer_count
    global user_count

    # Set up the screen from dimensions labled above
    screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="blue")

    # Set up the positioning of the images of rock, paper, and scissors
    rock(-300, 0)
    paper(0, 0)
    scissors(300, 0)

    #  For when either the computer or user has a count of 2 (or wins the game) the function will stop as there is no while statement for screen.mainloop(). This will end the game
    if computer_count == 2 or user_count == 2:
        screen.clear() # Clear the entire screen and setup an ending screen
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue") # Different color signifying end of game
        turtle.penup()
        turtle.home()
        turtle.color("red")
        turtle.write("GAME OVER. Thanks for playing!", False, "center", ("Times New Roman", 24, 'normal'))
        turtle.goto(0, -50)
        turtle.hideturtle()
    else: # This is the main part of this function and will default to this set of functions most often
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 250)
        turtle.color("white")
        turtle.write("Choose an option: (rock, paper, or scissors)", False, 'center', font)
        turtle.goto(0, 200)
        turtle.write("Rock[R], Paper[P], Scissors[S]", False, 'center', font)
        turtle.goto(-275, -250)
        turtle.write(f"Your score is: {user_count}", False, 'center', ("Arial", 18, 'normal')) # Displays user count
        turtle.goto(200, -250)
        turtle.write(f"Computer score is: {computer_count}", False, 'center', ("Arial", 18, 'normal')) # Displays computer count
        turtle.hideturtle()
    

        # Setup the onkeypress command for the user input
        wn = turtle.Screen()
        wn.listen() # Tell turtle to listen for a key press
        wn.onkeypress(Rock, 'r')
        wn.onkeypress(Scissors, 's')
        wn.onkeypress(Paper, 'p')

        # Make sure that while the game is continuing the screen is updating and in a mainloop
        while True:
            screen.update()
            screen.mainloop()

# Call the primary function: play()
play()