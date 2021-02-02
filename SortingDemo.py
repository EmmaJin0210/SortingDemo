"""
Program to demo different sorting algorithms through animation with Graphics.py
author: Emma Jin
date: 2020/01/16 - 2020/02/01
"""

from tile import*
from graphics import*
from time import sleep
from random import*


def bubbleSort(tiles):
    """
    demonstrate how bubble sort works with animation
    """
    done = False
    while not done:
        nswaps = 0
        for i in range(len(tiles)-1):
            tiles[i].setColor("light sky blue")
            sleep(0.4)
            if tiles[i] > tiles[i+1]:
                tiles[i].setColor("khaki")
                tiles[i+1].setColor("khaki")
                sleep(0.4)
                tiles[i],tiles[i+1] = tiles[i+1],tiles[i]
                tiles[i+1].move(50,0)
                tiles[i].move(-50,0)
                tiles[i].setColor("white")
                tiles[i+1].setColor("white")
                sleep(0.4)
                nswaps += 1
            tiles[i].setColor("white")
            sleep(0.4)
        if nswaps == 0:
            done = True

def insertionSort(tiles):
    """
    demonstrate how insertion sort works with animation
    """
    for i in range(1, len(tiles)):
        j = i
        while j > 0 and tiles[j] < tiles[j-1]:
            tiles[j].setColor("light sky blue")
            sleep(0.4)
            tiles[j].setColor("khaki")
            tiles[j-1].setColor("khaki")
            sleep(0.4)
            tiles[j],tiles[j-1] = tiles[j-1],tiles[j]
            tiles[j].move(50,0)
            tiles[j-1].move(-50,0)
            tiles[j].setColor("white")
            tiles[j-1].setColor("white")
            sleep(0.4)
            j =j - 1
        tiles[i].setColor("white")
        tiles[j].setColor("white")

def selectionSort(tiles):
    """
    demonstrate how selection sort works with animation
    """
    for j in range(len(tiles)):
        ios = j
        tiles[ios].setColor("green yellow") #smallest item so far
        sleep(0.4)
        for i in range(j+1,len(tiles)):
            tiles[i].setColor("light sky blue") #item currently being considered
            sleep(0.4)
            if tiles[i] > tiles[ios] or tiles[i] == tiles[ios]:
                tiles[i].setColor("white")
                sleep(0.4)
            else:
                tiles[ios].setColor("white")
                ios = i
                tiles[ios].setColor("green yellow")
                sleep(0.4)
        tiles[j].setColor("khaki") #items to be swapped
        tiles[ios].setColor("khaki")
        sleep(0.4)
        tiles[j],tiles[ios] = tiles[ios],tiles[j]
        d = ios - j
        tiles[j].move(-d*50,0)
        tiles[ios].move(d*50,0)
        sleep(0.4)
        tiles[j].setColor("white")
        tiles[ios].setColor("white")
################################################################################

def demonstrate(tiles, userinp):
    if userinp == 1:
        selectionSort(tiles)
    elif userinp == 2:
        insertionSort(tiles)
    elif userinp == 3:
        bubbleSort(tiles)
    else:
        return

def initializeTiles(gw):
    tiles = []
    for i in range(10):
        tiles.append(Tile(Point(25+50*i,75),50,"%d"%(randrange(100))))
    for item in tiles:
        item.draw(gw)
    return tiles

def initializeWin(typeSort):
     gw = GraphWin(typeSort,500,150)
     title = Text(Point(250,25),typeSort)
     title.setTextColor("black")
     title.setSize(30)
     title.draw(gw)
     return gw

def getTypeSort(userinp):
    if userinp == 1:
        typesort = "Selection Sort"
    elif userinp == 2:
        typesort = "Insertion Sort"
    elif userinp ==3:
        typesort = "Bubble Sort"
    else:
        return "Invalid Choice!"
    return typesort

def printMessage():
    print("""
    Choose from the 3 sorting algorithms below:
    1. Selection Sort
    2. Insertion Sort
    3. Bubble Sort
    """)
################################################################################

def main():
    printMessage()
    userinp = int(input("What sorting do you want to demonstrate? "))
    typesort = getTypeSort(userinp)
    gw = initializeWin(typesort)
    tiles = initializeTiles(gw)
    gw.getMouse()
    demonstrate(tiles,userinp)
    gw.getMouse()
    gw.close()

if __name__ == "__main__":
  main()
