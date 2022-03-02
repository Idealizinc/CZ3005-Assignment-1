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
from GreedyAlgorithm import Dijkstra

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
DEBUG_MODE_ON = True    # Enable or disable debug mode
DEBUG_ITERATION_MAX = 10 # Number of debug iterations to test for

# Main runtime
def main():
    # Load json into dict from file
    G = jsonLoadFromFile(JSON_PATH + FILE_G)
    Cost = jsonLoadFromFile(JSON_PATH + FILE_COST)
    Dist = jsonLoadFromFile(JSON_PATH + FILE_DIST)
    Coord = jsonLoadFromFile(JSON_PATH + FILE_COORD)

    # Perform Search Methods Here
    Dijkstra(G, Dist, 1,50)
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
