#!/usr/bin/env python3

from curses import *
from sys import *

# Other

s = initscr()
start_color()
use_default_colors()
noecho()
s.keypad(1)

fg, bg = 0, -1

for i in range(0, 256):
    init_pair(i + 1, i, bg)

# Varibles

# Buffers
fileBuff = [] # Entire file buffer
lineBuff = [] # Entire line buffer

# Other
maxY, maxX = s.getmaxyx() # Screen size
currY, currX = 0, 0 # Current coordinates
currLine = 0 # Current line
currLineIndex = 0 # Curent line index

# Functions

def updateArr(index, arr, arrApp): # Update arr at index
    del arr[index]
    arr.insert(index, arrApp)

def addArr(index, arr, arrApp):
    arr.insert(index, arrApp)

def updateScr(key):
    global currY, currX
    s.move(currY, currX)
    s.addstr(key)
    currX += 1

def main():
    pass

if __name__ == '__main__':
    main()
