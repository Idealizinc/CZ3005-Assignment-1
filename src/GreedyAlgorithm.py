'''
21S2 CZ3005 Assignment 1
Task 1
@author Li Zhaoyuan
@version 1.0
@since 2022-03-02
@modified 2022-03-02
'''
import sys
from queue import PriorityQueue
class Dijkstra:
    visitedV = []
    shortestD = []
    previousV = []
    #ShortestPath = ""

    def __init__(self):
        self.visitedV = []
        self.shortestD = []
        self.previousV = []



    def performSearch(self, startVertexStr, endVertexStr, g, dist):
        startVertex = int(startVertexStr)
        endVertex = int(endVertexStr)

        numV = len(g) #total number of Vertex
        shortestD = [sys.float_info.max] * (numV + 1) #initialise the shortest distance array with max values
        previousV = [-1] * (numV + 1) #previous vertices array
        visitedV = [False] * (numV + 1) #visited vertex array

        shortestD[startVertex] = 0 #first node dist is 0

        pqueue = PriorityQueue() #priority queue for greedy algo
        pqueue.put((0, str(startVertex))) #enqueue the first node in with the dist of 0

        while not pqueue.empty():
            currV = pqueue.get() #get the first vertex of the priority queue (shorest distance)
            visitedV[int(currV[1])] = True #set the current vertex that we are going to explore as visited
            for itr in range(len(g[currV[1]])): #go through all the adjacent vertices
                nextVertex = g[currV[1]][itr] #get the next vertex
                currWeight = float(dist[currV[1]+","+nextVertex]) #distance from current vertex to next vertex
                if currWeight > 0 and visitedV[int(nextVertex)] == False and \
                        shortestD[int(nextVertex)] > shortestD[int(currV[1])] + currWeight: #update path if the current vertex to the next vertex is the shorter one
                    shortestD[int(nextVertex)] = shortestD[int(currV[1])] + currWeight
                    previousV[int(nextVertex)] = int(currV[1])
                    pqueue.put((shortestD[int(nextVertex)], nextVertex)) #insert next vertex to the queue so that we can explore it as well

        resultStr = endVertexStr #end vertex
        currV = previousV[endVertex] #the connecting vertex
        while currV != -1 : #iterating thorught the array finding all the connecting vertex
            resultStr = str(currV) + "->" + resultStr
            currV = previousV[currV]
        print("Task 1 Greedy Path From ", startVertex,"to",endVertex) #print results
        print("Shortest path: " + resultStr)
        print("Shortest distance:", shortestD[endVertex])
        print("Total energy cost: nil")
