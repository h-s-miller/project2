# Project 2
Breadth-first search

# Description of BFS
Breadth-first search is an algorithm for pathfinding and traversal on unweighted graphs. "Breadth-first" refers to the method of traversing each layer of the graph before moving to the next layer. This method of traversal finds the shortest path between two nodes. 

# Algorithm 
My implementation of BFS uses a first-in-first-out queue to keep track of nodes to visit and a dictionary of parent nodes and a list of visited nodes to re-trace the path of traversal when the queue is finished. If there is an end node specified, and we reach it in the traversal, then we can break the queue early, as we have found the shortest path. If a path does not exist, the algorithm returns NONE. 

