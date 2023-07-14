import tkinter as tk
import random

window = tk.Tk()    #creates window

frame = tk.Frame(window)    #creates frame
frame.pack()

canvas = tk.Canvas(frame, width=400, height=300)    #creates canvas
canvas.pack()

balls = []
balls_coord1 = []
balls_coord2 = []
def create_ball(event):     #event is the coordinate of where button 1 is activated
    x = event.x             #x-coordinate
    y = event.y             #y-coordinate
    ball = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")      #Creates the ball
    balls_coord1.append((x,y))
    balls.append(ball)      #put the ball in a list
    print(balls_coord1)
canvas.bind("<Button-1>", create_ball)    #When button 1 is activated. Create_ball function is run.

def move_balls():
    for ball in balls:      #goes through every ball created
        dx = random.randint(-1,1)       #Creates a random x-coordinate
        dy = random.randint(-1,1)       #Creates a random y-coordinate
        canvas.move(ball,dx,dy)         #Moves the ball dx amount in x direction and dy amount in y direction.
        balls_coord2.append((dx,dy))
    canvas.after(100, move_balls)       #After 100 ms. Run move_balls again.
    print(balls_coord2)
#use interpolation to create smooth movement..

Simbutton = tk.Button(frame, text="Start Simulation", command= move_balls)   #button that runs function move_ball
Simbutton.pack()

#move_balls()

window.mainloop()

