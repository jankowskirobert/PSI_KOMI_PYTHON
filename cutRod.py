from Point import Point
from random import randrange
import numpy as np
from tkinter import *
from BruteForce import BruteForceMethod



def memorizedCutRod(p,n):
    memory = [-float("Inf")] * n
    return cutRod(p, memory, n)

def cutRod(p, memory, n):
    q = -float("Inf")
    if n == 0:
        q = 0
    if memory[n-1] >= 0:
        return memory[n-1];
    else:
        for i in range(1, n+1):
            tmp =  n-i;
            q = max(q, p[i-1]+cutRod(p, memory, tmp))
        memory[n-1] = q
    return memory[n-1]

def randomPoint():
    return Point(randrange(100,500, 10),randrange(100,500, 10))

def prepareArray(n):
    negihbourArray = np.zeros((n,n), float)
    np.fill_diagonal(negihbourArray, float("Inf"))
    print(negihbourArray)
    return negihbourArray

def fillArray(points, neighbourArray):
    compareMax = float("Inf")
    distance = 0;
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if j is not i:
                neighbourArray[i,j] = int(points[i].distanceTo(points[j]))


def removePath(neighbourArray, posI, posJ, colsRm, rowsRm):
    print("Got:")
    print(neighbourArray)

    neighbourArray[posJ, posI] = float("Inf")
    print("Deleting: "+str(posI)+" "+str(posJ))
    result = np.delete(neighbourArray, (posJ),1)
    result = np.delete(result, (posI),0)


    print("After:")
    print(result)
    return result

def printPoint(pathVisit, points):
    r = 5
    x = points[pathVisit[0]].getLocationX()
    y = points[pathVisit[0]].getLocationY()
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='red', fill='blue')
    Canevas.create_line(x, y,points[pathVisit[1]].getLocationX()
 , points[pathVisit[1]].getLocationY()
, fill="#476042")
    for i in range(1, len(pathVisit)-1):
        x = points[pathVisit[i]].getLocationX()
        y = points[pathVisit[i]].getLocationY()
        Canevas.create_oval(x-r, y-r, x+r, y+r, outline='blue', fill='blue')
        Canevas.create_line(x, y,points[pathVisit[i+1]].getLocationX()
 , points[pathVisit[i+1]].getLocationY()
, fill="#476042")


def findMinPath(neighbourArray, points, startPoint):
    visited = 1
    visitedArray = [False] * points
    visitedArray[startPoint] = True
    i = startPoint
    distance = 0
    paths = [startPoint]
    print(neighbourArray)
    while points != visited :
        j = 0
        maxVal = float("Inf")
        pointPosI = 0
        pointPosJ = 0 
        sizeLines = neighbourArray.shape[0]
        while j < sizeLines :
            tmpVal = neighbourArray[i, j]
            if tmpVal < maxVal and visitedArray[j] != True:
                maxVal = tmpVal
                pointPosJ = j
                pointPosI = i
            j += 1
        i = pointPosJ
        distance += maxVal
        visitedArray[i] = True
        visited += 1
        paths.append(i)
        print(str(i) + " " + str(maxVal))

    print("To start: " + str(neighbourArray[startPoint, i]))
    distance += neighbourArray[i, startPoint]
    return paths + [startPoint]



while True:
   # startPoint = Point(1,6)
   # endPoint = Point(7,6)
#    print(startPoint.distanceTo(endPoint))


    pointsList = [None] * 10
    for i in range(0, 10):
        pointsList[i] = randomPoint()

#    pointsList[0] = startPoint
#    pointsList[3] = endPoint

    print(*pointsList, sep="\n")

    br = BruteForceMethod([Point(5,4), Point(1,4), Point(4,2), Point(2,2), Point(1,1)])
    br.resolveProblem()
    arry = prepareArray(10)
    fillArray(pointsList, arry)
    print(arry)
    print("Result: ")

    path = findMinPath(arry, 10, 2)
    Mafenetre = Tk()
    Mafenetre.title('Cercle')

# Création d'un widget Canvas (zone graphique)
    Largeur = 580
    Hauteur = 520
    Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    Canevas.pack(padx =5, pady =5)
    printPoint(path, pointsList)
    print("Size: "+str(path))
    if path == float("Inf") or True:
        break
p = [1,5,8,9]
out = memorizedCutRod(p, 4)
print(out)
Mafenetre.mainloop()

