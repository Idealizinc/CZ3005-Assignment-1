'''
Task 2 : Uniform Cost Search
@author Lim Rui An, Ryan
@version 1.0
@since 2022-03-02
@modified 2022-03-02
'''

# Import of necessary dependencies
from queue import PriorityQueue
import sys


# Find the shortest path between 2 locations within EnergyBudget
class UniformCostSearch:
    ExploredSet = None
    TotalDistance = None
    TotalEnergy = None
    ShortestPath = ""

    def __init__(self):
        self.ExploredSet = None
        self.TotalDistance = None
        self.TotalEnergy = None
        self.ShortestPath = ""

    def performSearch(self, StartNode, EndNode, EnergyCap, G, Cost, Dist):
        # Set up a PriorityQueue to be used as our frontier of nodes to be explored
        Frontier = PriorityQueue()

        # Initialize the frontier by inserting the start node
        Frontier.put((0, 0, StartNode)) # Tuple of (Distance,Energy,Node)

        # Initiallize other required parameters
        Explored = {}           # Dict of explored nodes combined with energy costs {(node,cost) : parentNode}
        ExploredDistance = {}   # Dict of explored distances {(node,cost) : parentNode}

        # For a single node
        DistCost = {}           # Dict of dist cost from start to current node {node : cost}
        EnergyCost = {}         # Dict of energy cost from start to current node {node : cost}

        # For every Node,EnergyCost combination we store the minimal distance to get to the node with this specific energy
        Explored[(StartNode, 0)] = None         # No previous edge linking to the starting node
        ExploredDistance[(StartNode, 0)] = 0    # The starting node has a travel distance of 0

        # Repeat the process until either the frontier is empty or the goal has been reached
        while not Frontier.empty():
            # Get the first vertex in the frontier to be explored and its properties
            currDist, currEnergy, currNode = Frontier.get()

            # Check if the stored distance and energy is lower than what this current node offers
            if (currNode in DistCost and currNode in EnergyCost) and (DistCost[currNode] <= currDist and EnergyCost[currNode] <= currEnergy):
                continue # Skip the current node from the frontier as it will not lead to a shorter path
            else: # Update the distances and costs when there is a better one found
                if currNode not in DistCost or DistCost[currNode] > currDist:
                    DistCost[currNode] = currDist
                if currNode not in EnergyCost or EnergyCost[currNode] > currEnergy:
                    EnergyCost[currNode] = currEnergy

            # Check if the current node is the goal
            if currNode == EndNode:
                break

            # If yet to reach goal, explore all neighbours adjacent to current node
            neighbours = G[currNode]
            for next in neighbours: # Explore all adjacent nodes
                # Get properties between current node to its neighbour
                pair = currNode + "," + next
                dist = Dist[pair]
                energy = Cost[pair]
                # Calculate total costs based on current node
                newDist = dist + currDist
                newEnergy = energy + currEnergy
                # Consider whether to explore this node
                # Either unexplored or new energy cost acceptable, if too high, don't explore
                if next not in Explored and newEnergy <= EnergyCap:
                    # Insert the next node into the frontier, with its distance as the exploration prioity
                    Frontier.put((newDist, newEnergy, next))
                    # Store its costs
                    ExploredDistance[(next, newEnergy)] = newDist
                    # Update the exploration status and set the current node to be the exploration parent node
                    Explored[(next, newEnergy)] = (currNode, currEnergy)

        # Store calculated data into class
        self.ExploredSet = Explored
        self.TotalDistance = ExploredDistance[(EndNode, EnergyCost[EndNode])]
        self.TotalEnergy = EnergyCost[EndNode]
        self.setupExplorationResultString(EndNode, EnergyCost[EndNode])
        return self

    def setupExplorationResultString(self, EndNode, Cost):
        result = ""
        current = self.ExploredSet[(EndNode, Cost)]
        while current != None:
            result = current[0] + "->" + result
            current = self.ExploredSet[current]
        self.ShortestPath = result + EndNode
        return self

    def printResults(self):
        print("Shortest Path: " + self.ShortestPath)
        print("Shortest Distance: " ,self.TotalDistance)
        print("Total Energy Cost: " , self.TotalEnergy)
