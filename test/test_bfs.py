import pytest
from search import graph
import networkx as nx

"""
Functions for testing breadth-first search function by testing on dummy network:
            A
         /    \   
        v      v    
        B       C
      /   \    /  \
      v    v   v  v
      D    E   F  G

"""

def test_bfs_traversal():
    """
    Check if function is traversing breadth-first properly
    Starting with A, it should go layer by layer: A, B, C, D, E, F, G
    """
    g=graph.Graph('dummy.adjlist')
    trav=g.bfs('A')
    assert trav == ['A','B','C','D','E','F','G']

def test_bfs_path_exists():
    """
    Check if function finds the shortest path between start and end node
    Starting with A and going to D, the shortest path is A->B->D
    """
    g=graph.Graph('dummy.adjlist')
    shortest_path=g.bfs('A','D')
    assert shortest_path == ['A','B','D']

def test_bfs_path_DNE():
    """
    Check if function finds returns None if no path exists between two nodes
    There is no path between D and G, so function should return None
    """
    g=graph.Graph('dummy.adjlist')
    non_path=g.bfs('D','G')
    assert non_path == None

