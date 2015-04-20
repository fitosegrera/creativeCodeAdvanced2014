from Tkinter import *

import random
import time

# create the matrices
cell = [[0 for row in range(-1,61)] for col in range(-1,81)]
live = [[0 for row in range(-1,61)] for col in range(-1,81)]
temp = [[0 for row in range(-1,61)] for col in range(-1,81)]

# process and draw the next frame
def frame():
    process()
    draw()
    root.after(100, frame)

# load the initial data
def load():
    for y in range(-1,61):
        for x in range(-1,81):
            live[x][y] = 0
            temp[x][y] = 0
            cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black")

    # GLIDER in 10,10
    live[11][10] = 1
    live[12][11] = 1
    live[10][12] = 1
    live[11][12] = 1
    live[12][12] = 1
    live[13][12] = 1
    live[13][13] = 1
    live[13][14] = 1
    live[14][13] = 1
    live[14][14] = 1
    live[14][15] = 1
    live[15][14] = 1

    # GLIDER in 30,30
    live[31][30] = 1
    live[32][31] = 1
    live[30][32] = 1
    live[31][32] = 1
    live[32][32] = 1

# Apply the 4 rules to the matrix
def process():
    for y in range(0,60):
        for x in range(0,80):
            lives = live_neighbors(x,y)
            # Rule 1 - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
            if live[x][y] == 1 and lives < 2: temp[x][y] = 0
            # Rule 2 - Any live cell with two or three live neighbours lives on to the next generation.
            if live[x][y] == 1 and (lives == 2 or lives == 3): temp[x][y] = 1
            # Rule 3 - Any live cell with more than three live neighbours dies, as if by overcrowding.
            if live[x][y] == 1 and lives > 3: temp[x][y] = 0
            # Rule 4 - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if live[x][y] == 0 and lives == 3: temp[x][y] = 1

    for y in range(0,60):
        for x in range(0,80):
            live[x][y] = temp[x][y]

# Count live neighbors
def live_neighbors(a,b):
    lives = 0
    if live[a-1][b+1] == 1: lives = lives + 1
    if live[a][b+1] == 1: lives = lives + 1
    if live[a+1][b+1] == 1: lives = lives + 1
    if live[a-1][b] == 1: lives = lives + 1
    if live[a+1][b] == 1: lives = lives + 1
    if live[a-1][b-1] == 1: lives = lives + 1
    if live[a][b-1] == 1: lives = lives + 1
    if live[a+1][b-1] == 1: lives = lives + 1
    return lives

# Draw all cells
def draw():
    for y in range(60):
        for x in range(80):
            if live[x][y]==0:
                canvas.itemconfig(cell[x][y], fill="black")
            if live[x][y]==1:
                canvas.itemconfig(cell[x][y], fill="green")

# main loop
root = Tk()
root.title("Conway's Game of Life")
canvas = Canvas(root, width=800, height=600, highlightthickness=0, bd=0, bg='black')
canvas.pack()
load()
frame()
root.mainloop()