import tkinter as tk
import random

window = tk.Tk()    #creates window

frame = tk.Frame(window)    #creates frame
frame.pack()

canvas = tk.Canvas(frame, width=600, height=600)    #creates canvas
canvas.pack()

balls = []
balls_coord1 = []
balls_coord2 = []
def create_ball(event):     #event is the coordinate of where button 1 is activated
    global balls
    x = event.x             #x-coordinate
    y = event.y             #y-coordinate
    r = random.randint(10,30) #randomize the radius of each ball between 10 and 30
    color = random.choice(["red","green","blue","yellow","black"])
    ball_nr = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)      #Creates the ball
    balls_coord1.append((x,y))
    dx = dy = 0 #Declares random speed in x direction
           #Declares random speed in y direction
    while dx == 0 or dy == 0:
        dx = random.randint(-2,2)
        dy = random.randint(-2,2)

    balls.append((ball_nr,x,y,r,dx,dy))      #put the ball in a list with all its qualities
    #print(balls_coord1)
canvas.bind("<Button-1>", create_ball)    #When button 1 is activated. Create_ball function is run.

def move_balls():
    global balls
    for ball in balls:     #goes through every ball create
        ball_nr,x,y,r,dx,dy = ball #Initialize the current values
        canvas.move(ball_nr,dx,dy)         #Moves the ball dx amount in x direction and dy amount in y direction.
        x+=dx #updates x pos
        y+=dy #updates y pos
        if x - r <= 0 or x + r >= int(canvas["width"]): #checks if all touches border
            dx *= -1
        if y - r <= 0 or y + r >= int(canvas["height"]): #---II---
            dy *= -1
        balls[balls.index(ball)] = (ball_nr, x, y, r, dx, dy) #updates values of current ball
        balls_coord2.append((x+dx,y+dy))
    canvas.after(40, move_balls)       #After 100 ms. Run move_balls again.
    #print(balls_coord2)
#use interpolation to create smooth movement..

Simbutton = tk.Button(frame, text="Start Simulation", command= move_balls)   #button that runs function move_ball
Simbutton.pack()

#move_balls()

window.mainloop()

