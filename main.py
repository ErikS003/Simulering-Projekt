import tkinter as tk
window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

canvas = tk.Canvas(frame, width=400, height=300)
canvas.pack()

button = tk.Button(frame, text="Start Simulation")
button.pack()

#button.bind("", lambda event: func())

window.mainloop()

