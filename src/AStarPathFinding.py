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

        # Initialize the frontier by inserting the start node
        Frontier.put([0, StartNode])

        # Initiallize other required parameters
        Explored = {}  # Dict of explored nodes {node : parentNode}
        DistCost = {}  # Dict of dist cost from start to end node {node : cost}
        FCost = {}  # Dict of dict cost + heuristic cost from start to end node {node : cost}
        EnergyCost = {}  # Dict of energy cost from start to end node {node : cost}

        # Initiallize values for starting node
        Explored[StartNode] = None  # Start node no parent
        DistCost[StartNode] = 0  # Start to Start cost = 0
        FCost[StartNode] = 0
        EnergyCost[StartNode] = 0  # Start to Start cost = 0

        # Repeat the process until either the frontier is empty or the goal has been reached
        while not Frontier.empty():
            current = Frontier.get()[
                1]  # Get the first vertex in the frontier to be explored ([1] is used to get the node id)
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
                newDist = DistCost[current] + dist
                newFCost = newDist #+ (self.heuristic(current, next, Coord))
                newEnergy = EnergyCost[current] + energy

                # Consider whether to explore this node
                # Either unexplored or the new costs to this node is better than the recorded ones
                if(next not in FCost):
                    FCost[next] = sys.float_info.max
                if (next not in Explored) and (newFCost < FCost[next]):
                    # Check energy cost, if too high, don't explore
                    if newEnergy <= EnergyCap:
                        # Insert the next node into the frontier, with its distance as the exploration prioity
                        Frontier.put((newFCost, next))
                        # Store its costs
                        FCost[next] = newFCost
                        DistCost[next] = newDist
                        EnergyCost[next] = newEnergy
                        # Update the exploration status and set the current node to be the exploration parent node
                        Explored[next] = current

        # Store calculated data into class
        self.ExploredSet = Explored
        self.TotalDistance = DistCost[EndNode]
        self.TotalEnergy = EnergyCost[EndNode]
        self.setupExplorationResultString(EndNode)
        return self

    def setupExplorationResultString(self, EndNode):
        result = ""
        current = self.ExploredSet[EndNode]
        while current != None:
            result = current + "->" + result
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
