'''
Task 3 : AStar Pathfinding
@author Lim Rui An, Ryan , Li Zhaoyuan
@version 1.0
@since 2022-03-02
@modified 2022-03-02
'''

# Import of necessary dependencies
from queue import PriorityQueue
import sys
import math


# Find the shortest path between 2 locations within EnergyBudget
class AStarPathFinding:
    ExploredSet = None
    TotalDistance = None
    TotalEnergy = None
    ShortestPath = ""

    def __init__(self):
        self.ExploredSet = None
        self.TotalDistance = None
        self.TotalEnergy = None
        self.ShortestPath = ""

    def performSearch(self, StartNode, EndNode, EnergyCap, G, Cost, Dist, Coord):
        # Set up a PriorityQueue to be used as our frontier of nodes to be explored
        Frontier = PriorityQueue()

        # Initialize the frontier by inserting the start node with 0 energy cost, 0 distance and 0 priority(fCost from g + h)
        #each element is in the order of (priority,distance,(node, cost))
        Frontier.put((0, 0, (StartNode, 0)))

        # Initiallize other required parameters
        Explored = {}  # Dict of explored nodes {node : parentNode}
        DistCost = {}  # Dict of dist cost from start to end node {node : cost}
        minCost = {}  # Dict to store the lowest cost for the specific node
        minDist = {}  # Dict to store the lowest dist for the specific node

        # Initiallize values for starting node
        Explored[(StartNode, 0)] = None  # Start node no parent

        DistCost[(StartNode, 0)] = 0  # Start to Start cost = 0

        # Repeat the process until either the frontier is empty or the goal has been reached
        while not Frontier.empty():
            currentP, currentDist, (current, currentCost) = Frontier.get()  # Get the first vertex in the frontier to be explored ([1] is used to get the node id)

            # If there exist a short path to current node/vertex we can go to check the next element in the priority queue
            if current in minDist and current in minCost and minDist[current] <= currentDist and minCost[current] <= currentCost:
                continue
            # Update the min dictionary for dist and cost when there exist a better Distance or better Energy cost to the current node that we are visiting
            if current not in minDist or minDist[current] > currentDist:
                minDist[current] = currentDist
            if current not in minCost or minCost[current] > currentCost:
                minCost[current] = currentCost

            # Check if the current node is the goal
            if current == EndNode:
                break
            # If yet to reach goal, explore all neighbours adjacent to current node
            neighbours = G[current]
            for next in neighbours:  # Explore all adjacent nodes
                # Get cost for this new node
                dist = Dist[current + "," + next]
                energy = Cost[current + "," + next]
                # Calculate total costs based on current node
                newDist = DistCost[(current, currentCost)] + dist
                newEnergy = currentCost + energy

                # Consider whether to explore this node
                # Either unexplored or the new costs to this node is better than the recorded ones
                # Check energy cost, if too high, don't explore
                if (next, newEnergy) not in Explored and newEnergy <= EnergyCap:
                    # calculate the A*'s FCost to be used as Priority
                    priority = newDist + (self.heuristic(current, next, Coord))
                    # Insert the next node into the frontier, with its fCost as the exploration priority
                    Frontier.put((priority, newDist, (next, newEnergy)))
                    # Store its costs
                    DistCost[(next, newEnergy)] = newDist

                    # Update the exploration status and set the current node to be the exploration parent node
                    Explored[(next, newEnergy)] = (current, currentCost)

        for itr in DistCost:
            if itr[0] == '50':
                print(DistCost[itr[0], minCost['50']])
                print(minCost['50'])
        # Store calculated data into class
        self.ExploredSet = Explored
        self.TotalDistance = DistCost[EndNode,minCost[EndNode]]
        self.TotalEnergy = minCost[EndNode]
        self.setupExplorationResultString(EndNode,minCost[EndNode])
        return self

    def setupExplorationResultString(self, EndNode, MinCost):
        result = ""
        current = self.ExploredSet[EndNode, MinCost]
        while current != None:
            result = current[0] + "->" + result
            current = self.ExploredSet[current]
        self.ShortestPath = result + EndNode
        return self

    def printResults(self):
        print("Shortest Path: " + self.ShortestPath)
        print("Shortest Distance: ", self.TotalDistance)
        print("Total Energy Cost: ", self.TotalEnergy)

    def heuristic(self, hereVertex, thereVertex, coord):
        hereCoord = coord[hereVertex]
        thereCoord = coord[thereVertex]

        hypotenuseSq = pow(thereCoord[0] - hereCoord[0], 2) + pow(thereCoord[1] - hereCoord[1], 2)

        return math.sqrt(hypotenuseSq)
