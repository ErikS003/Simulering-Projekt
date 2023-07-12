import tkinter as tk
window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

canvas = tk.Canvas(frame, width=400, height=300)
canvas.pack()

Simbutton = tk.Button(frame, text="Start Simulation")
Simbutton.pack()


def create_ball(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")  
canvas.bind("<Button-1>", create_ball)  

#button.bind("", lambda event: func())

window.mainloop()

