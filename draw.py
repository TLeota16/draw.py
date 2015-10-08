import turtle

def draw_square(some_turtle):
    for x in range(0, 4):
    
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Write Initials (T)
    T = turtle.Turtle()
    T.shape("arrow")
    T.speed(2)
    T.forward(100)
    T.backward(50)
    T.right(90)
    T.forward(100)

    #Write Initials (L)
    L = turtle.Turtle()
    L.shape("circle")
    L.speed(2)
    L.penup()
    L.goto(105, 0)
    L.pendown()
    L.right(90)
    L.forward(100)
    L.left(90)
    L.forward(75)
    
    
    #Create Brad - Square
    #brad = turtle.Turtle()
    #brad.shape("turtle")
    #brad.speed(10)
    #for i in range(0,36):
        #draw_square(brad)
        #brad.right(10)
    
 

    
    #Create Angie - Circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #Create Tuli - Triangle
    #tuli = turtle.Turtle()
    #tuli.shape("circle")
    #tuli.color("green")

    #for x in range(0, 3):
        #tuli.forward(100)
        #tuli.left(120)

    window.exitonclick()


draw_art()
