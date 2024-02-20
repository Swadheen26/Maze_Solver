'''
->First funtion to create maze board size (n*n)
->Top left corner i.e Start and Bottom right corner i.e End represented by "S" and "E" with green color.
UNIQUE CODE:
for Walls :Full block(U+2593) (Red)
for Open space :Dotted circle(U+25CC)(Blue)
for Path : Circle With Vertical Fill(U+25CD)(Green)
'''
from colorama import Fore
import random
from collections import deque

def mazeCreate(n):
    maze = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 and j == 0:
                row.append(Fore.GREEN + "S" + Fore.RESET)   #Start point (S) 
            elif i == n - 1 and j == n- 1:
                row.append(Fore.GREEN + "E" + Fore.RESET)   #End point (E)
            else:
                row.append(Fore.BLUE + u"\u25cc" + Fore.RESET)
        maze.append(row)