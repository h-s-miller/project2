import networkx as nx
from queue import Queue

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Method that performs a breadth first traversal and pathfinding on graph G
        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """

        #check edge cases
        # case: start node not in the graph, return error
        if start not in self.graph.nodes:
            raise ValueError("Start node not in graph")

        # case: end node not in the graph, return error
        if (end != None) and (end not in self.graph.nodes):
            raise ValueError("End node not in graph")
        
        
        visited=[]
        queue= []

        queue.append(start)
        visited.append(start)

        parent=dict()
        parent[start]=None

        path_found=False
        while queue:
            current_node=queue.pop(0) #dequeue current node 

            if end:
                if current_node == end: #if end node defined, and we can break traversal if we reach the end node
                    path_found=True
                    break

            for next_node in self.graph[current_node]: #visit all daughter nodes of current node
                if next_node not in visited: #check if visited already
                    queue.append(next_node) #add into queue
                    parent[next_node]=current_node #keep track of parents for pathfinding 
                    visited.append(next_node)

        # if we are looking for a path, and we know the path exists from the traversal,
        # then we need to retrace the path using the parent dictionary
        if end and path_found:
            path=[]
            if path_found:
                target_node=end
                path.append(target_node) #start at target node
                while parent[target_node] is not None:
                    path.append(parent[target_node])
                    target_node=parent[target_node] #update on parent
                path.reverse() #since i went backwards, need to reverse the path 
            return path
        
        #if we are looking for path, but it does not exist, return none
        elif end and not path_found:
            return None
        
        #if we are not looking for a path, we just return the order of the traversal
        else:
            return visited
    
