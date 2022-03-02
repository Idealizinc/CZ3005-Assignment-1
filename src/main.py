'''
21S2 CZ3005 Assignment 1
Finding a Shortest Path with An Energy Budget
@author Lim Rui An, Ryan & Li Zhaoyuan
@version 1.0
@since 2022-03-02
@modified 2022-03-02
'''
# Import of necessary dependencies
import json # To process json data from given files

# Import of search algorithms
from GreedyAlgorithm import Dijkstra
from UniformCostSearch import UniformCostSearch

# Constants
JSON_PATH = "../json/"
FILE_G = "G.json"
FILE_COST = "Cost.json"
FILE_DIST = "Dist.json"
FILE_COORD = "Coord.json"

# Global json data
G = None     # Graph dictionary
Cost = None  # Edge cost dictionary
Dist = None  # Edge distance dictionary
Coord = None # Node coordination dictionary

# Settings
DEBUG_MODE_ON = False    # Enable or disable debug mode
DEBUG_ITERATION_MAX = 10 # Number of debug iterations to test for

# Main runtime
def main():
    # Load json into dict from file
    G = jsonLoadFromFile(JSON_PATH + FILE_G)
    Cost = jsonLoadFromFile(JSON_PATH + FILE_COST)
    Dist = jsonLoadFromFile(JSON_PATH + FILE_DIST)
    Coord = jsonLoadFromFile(JSON_PATH + FILE_COORD)

    # Set up starting and ending nodes with energy Budget
    Start = "1"
    End = "50"
    EnergyBudget = 287932

    # Test Case
    if DEBUG_MODE_ON:
        G = {"4": ["1", "2", "3"], "1": ["5"], "2": ["5"], "3": ["5"], "5": []}
        Dist = {"4,1": 4, "1,5": 8, "4,2": 2, "2,5": 8, "4,3": 4, "3,5": 12}
        Cost = {'4,1' : 7, '1,5' : 3, '4,2' : 6, '2,5': 6, '4,3' : 3, '3,5' : 2}
        Start = "4"
        End = "5"
        EnergyBudget = 11

    # Perform Search Methods Here
    Dijkstra(G, Dist, Start,End)
    # Task 2
    UniformCostSearch().performSearch(Start, End, EnergyBudget, G, Cost, Dist).printResults()
    return

# Task 1: Any search with no energy constraint

# Task 2: Any uninformed search algorithm

# Task 3: A* search algorithm

def jsonLoadFromFile(PATH):
    # Open JSON file
    f = open(PATH)
    # Load JSON object as a dictionary
    data = json.load(f)
    # For debugging, note the JSON files are HUGE, do not try and print everything
    if DEBUG_MODE_ON:
        print("\n> Debug Preview Output: " + PATH)
        i = 0
        for attribute, value in data.items(): # Iterate through the json
            print(attribute, value)
            i += 1 # Note no ++ in python
            if i  >= DEBUG_ITERATION_MAX:
                break
    # Close file when done
    f.close()
    print("> File: <" + PATH + "> Loaded Successfully")
    # Return parsed data
    return data

if __name__ == "__main__":
    main()
