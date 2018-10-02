# Name: Rezaee, Milad
# Student Number: 300069170
# Course:  IT1 1120
# Assignment Number 1

import math
import turtle
###################################################################
# Question 1
###################################################################

def pythagorean_pair(a,b):
    """returns True if integers a and b have a third integer as the pythagorean pair
    , False if integers a and b do not have a third integer as the pythagorean pair"""
    c = math.sqrt((a**2) + (b**2))
    decimal_is_zero = (c - math.floor(c)) == 0
    return decimal_is_zero

###################################################################
# Question 2
###################################################################

def mh2kh(s):
    """returns the kilometers per hour conversion of the parameter s which is given in
    miles per hour"""
    return  s * 1.609344

###################################################################
# Question 3
###################################################################

def in_out(xs,ys,side):
    """returns True if user inputted coordinates is inside the square defined by the
    function parameters. (xs, ys) is a point with "side" length and "side" wide creating
    a square"""
    x_coord = float(input("Enter a number for the x coordinate of a query point: "))
    y_coord = float(input("Enter a number for the y coordinate of a query point: "))

    return ((x_coord <= (xs + side) and x_coord >= xs)
            and (y_coord <= (ys + side) and y_coord >= ys))

###################################################################
# Question 4
###################################################################

def safe(n):
    """returns True if the integer n cannot be divided by 9, or does not contain the
    digit 9. Returns False otherwise"""
    first_digit = math.floor(n/10)
    second_digit = n - (math.floor(n/10) * 10)
    return (n%9 != 0 and (first_digit != 9 and second_digit != 9))

###################################################################
# Question 5
###################################################################

def quote_maker(quote, name, year):
    """returns an organised string that states a quote, name of the quoter, and the year
    the quote was said"""
    return f"In {year} a person called {name} said: \"{quote}\""

###################################################################
# Question 6
###################################################################

def quote_displayer():
    """asks the user for the quote, name, and year and uses the quote_maker() function to
    return an organised version of the quote"""
    quote = input("Give me a quote: ") 
    name = input("Who said that? ")
    year = input("What year did she/he say that? ")

    return quote_maker(quote, name, year)

###################################################################
# Question 7
###################################################################

def rps_winner():
    """returns True/False whether Player 1 wins in a game of rock, paper, scissors and if
    the game was a tie"""
    print("What choice did player 1 make?")
    player_1 = input("Type one of the following options: rock, paper, scissors: ")
    print("What choice did player 2 make?")
    player_2 = input("Type one of the following options: rock, paper, scissors: ")

    winner = ((player_1 == "rock" and player_2 == "scissors") or (player_1 == "paper" and player_2 == "rock") or (player_1 == "scissors" and player_2 == "paper"))

    tie = not ((player_1 == "rock" and player_2 == "rock") or (player_1 == "paper" and player_2 == "paper") or (player_1 == "scissors" and player_2 == "scissors"))

    print(f"Player 1 wins. That is {winner}")
    print(f"It is a tie. That is not {tie}")

###################################################################
# Question 8
###################################################################

def fun(x):
    """returns the value of y of the equation 10^(4y)=x+3 with the given parameter x"""
    return (math.log10(x+3))/4

###################################################################
# Question 9
###################################################################

def ascii_name_plaque(name):
    """returns an ascii version of the inputed name with "*" borders"""
    print("*" * (len(name)+10))
    print("*" + (" "* (len(name) + 8)) + "*")
    print("*  __" + name + "__  *" )
    print("*" + (" "* (len(name) + 8)) + "*")
    print("*" * (len(name)+10))

###################################################################
# Question 10
###################################################################

def draw_car():
    """returns a turtle drawing of a car"""
    s=turtle.Screen() 
    t=turtle.Turtle() 

    ###################################
    #Bottom of car

    t.setheading(180) 

    t.up()
    t.pencolor("black")
    t.goto(83, -110)
    t.pendown()

    t.forward(177)
    ####################################
    #BOTTOM

    t.up()
    t.goto(237, -110)
    t.pendown()

    t.forward(40)

    t.up()
    t.goto(-207, -110)
    t.pendown()

    t.forward(40)
    ####################################
    #BOTTOM-TOP

    t.up()
    t.pencolor("black")
    t.goto(245, -70)
    t.pendown()

    t.forward(50)

    t.up()
    t.goto(-207, -70)
    t.pendown()

    t.forward(50)
    ####################################
    #DIAGONAL

    t.left(-102)

    t.up()
    t.goto(237, -110)
    t.pendown()

    t.forward(40)

    t.left(25)

    t.up()
    t.goto(-247, -110)
    t.pendown()

    t.forward(40)
    ####################################
    #COLOR

    t.color("blue")
    t.begin_fill()
    t.up()
    t.goto(-247, -110)
    t.pendown()

    t.up()
    t.goto(237, -110)
    t.pendown()

    t.up()
    t.goto(245, -70)
    t.pendown()

    t.up()
    t.goto(-257, -70)
    t.pendown()
    t.end_fill()
    ####################################
    #FRONT

    t.setheading(90)

    t.up()
    t.goto(225, -70)
    t.pendown()

    t.forward(80)
    t.setheading(-90)
    ####################################
    #CAR MIDDLE

    t.setheading(180)

    t.up()
    t.goto(225, 10)
    t.pendown()

    t.forward(460)
    ####################################
    #BACK

    t.setheading(90)

    t.up()
    t.goto(-235, -70)
    t.pendown()

    t.forward(80)
    ####################################
    #COLOR

    t.color("blue")
    t.begin_fill()
    t.up()
    t.goto(-235, -70)
    t.pendown()

    t.up()
    t.goto(225, -70)
    t.pendown()

    t.up()
    t.goto(225, 10)
    t.pendown()

    t.up()
    t.goto(-235, 10)
    t.pendown()
    t.end_fill()
    ####################################
    #CAR TOP

    t.setheading(180)

    t.up()
    t.goto(50, 120)
    t.pendown()

    t.forward(160)
    ####################################
    #FRONT PANE

    t.left(115)

    t.up()
    t.goto(50, 120)
    t.pendown()

    t.forward(121)
    ####################################
    #BACK PANE

    t.left(-50)

    t.up()
    t.goto(-110, 120)
    t.pendown()

    t.forward(121)
    ####################################
    #MIDDLE DOOR

    t.setheading(90)

    t.up()
    t.pencolor("black")
    t.goto(-50, -110)
    t.pendown()

    t.forward(230)
    ####################################
    #MIDDLE DOOR FRONT

    t.up()
    t.goto(100, -50)
    t.pendown()

    t.forward(60)
    ####################################
    #DOOR HANDLE

    t.up()
    t.goto(-10, -10)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.end_fill()
    ####################################
    #REAR LIGHTS

    t.up()
    t.pencolor("red")
    t.goto(-215, -10)
    t.pendown()

    t.color("red")
    t.begin_fill()
    t.forward(13)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(13)
    t.left(90)
    t.forward(20)
    t.end_fill()

    t.setheading(-360)
    ####################################
    #LEFT WHEEL

    t.penup()
    t.goto(-150, -150)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    t.penup()
    t.goto(-150, -120)
    t.pendown()

    t.color("grey")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(-150, -95)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    ####################################
    #WHEEL SPIKES LEFT

    t.penup()
    t.pencolor("red")
    t.goto(-150, -85)
    t.pendown()

    t.left(90)
    t.forward(25)

    t.penup()
    t.goto(-155, -90)
    t.pendown()

    t.left(70)
    t.forward(25)

    t.penup()
    t.goto(-153, -95)
    t.pendown()

    t.left(70)
    t.forward(25)

    t.penup()
    t.goto(-147, -95)
    t.pendown()

    t.left(80)
    t.forward(25)

    t.penup()
    t.goto(-145, -90)
    t.pendown()

    t.left(80)
    t.forward(25)

    t.left(-10)
    ####################################
    #RIGHT WHEEL

    t.penup()
    t.pencolor("black")
    t.goto(160, -150)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    t.penup()
    t.goto(150, -120)
    t.pendown()

    t.color("grey")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(140, -95)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    ####################################
    #WHEEL SPIKES RIGHT

    t.setheading(90)

    t.penup()
    t.pencolor("red")
    t.goto(140, -85)
    t.pendown()

    t.forward(23)

    t.penup()
    t.goto(133, -90)
    t.pendown()

    t.left(70)
    t.forward(22)

    t.penup()
    t.goto(135, -95)
    t.pendown()

    t.left(70)
    t.forward(25)

    t.penup()
    t.goto(143, -95)
    t.pendown()

    t.left(80)
    t.forward(25)

    t.penup()
    t.goto(143, -88)
    t.pendown()

    t.left(80)
    t.forward(25)

    t.left(-10)
    ####################################
    #FRONT LIGHTS

    t.up()
    t.pencolor("black")
    t.goto(215, -15)
    t.pendown()

    t.left(-20)

    t.shape("circle")
    t.shapesize(1.4, 0.5)
    t.fillcolor("yellow")
    ####################################

    turtle.exitonclick()

###################################################################
# Question 11
###################################################################

def alogical(n):
    """returns the minumum number of times it takes the number n to be divided by 2 in order to
    result in a number less than or equal to 1"""
    return round(math.log(n + 1,2))

###################################################################
# Question 12
###################################################################

def time_format(h,m):
    """returns a fancy way of telling time of the inputted hours(h) and minutes(m)"""
    minute = int(round(m/5.0)*5.0)

    if minute == 0:
      print(str(h) + " o’clock")
    elif minute == 60:
      if h < 23:
        print(str(h + 1) + " o'clock")
      else:
        print("0 o'clock")
    elif minute == 30:
      print("half past " + str(h) + " o'clock")
    elif minute < 30:
      print(str(minute) + " minutes past " + str(h) + " o'clock")
    elif minute > 30:
      if h < 23:
        print(str(60 - minute) + " minutes to " + str(h + 1) + " o'clock")
      else:
        print(str(60 - minute) + " minutes to 0 o'clock")

###################################################################
# Question 13
###################################################################

def cad_cashier(price,payment):
    """returns the amount of change(in Canadian dollars) needed after a payment is made for a certain price"""
    price = round(price*100/5) * 5/100
    return round(payment - price, 2)

###################################################################
# Question 14
###################################################################

def min_CAD_coins(price,payment):
    """uses the cad_cashier() function to determine how much change is required and returns the least number
    of toonies, loonies, quarters, dimes and nickles possible in a tuple of (t, l, q, d, n)"""
    change = round((cad_cashier(price,payment)) * 100)
	
    t = math.floor(change / 200)
    change -= t * 200
    l = math.floor(change / 100)
    change -= l * 100
    q = math.floor(change / 25)
    change -= q * 25
    d = math.floor(change / 10)
    change -= d * 10
    n = math.floor(change / 5)

    return (t, l, q, d, n)


