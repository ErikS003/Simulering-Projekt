import tkinter as tk
import random
window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

canvas = tk.Canvas(frame, width=400, height=300)
canvas.pack()

Simbutton = tk.Button(frame, text="Start Simulation")
Simbutton.pack()

balls = []
def create_ball(event):
    x = event.x
    y = event.y
    ball = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
    balls.append(ball) 
canvas.bind("<Button-1>", create_ball)

def move_balls():
    for ball in balls:
        dx = random.randint(-3,3)
        dy = random.randint(-3,3)
        canvas.move(ball,dx,dy)
    window.after(100, move_balls)
#use interpolation to create smooth movement..
move_balls()

window.mainloop()

