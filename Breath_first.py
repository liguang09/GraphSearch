from re import T
from typing import Dict, List, Protocol, TypeVar


Location = TypeVar('Location')
class Graph(Protocol):
    def neighbors(self, id: Location)-> List[Location]:pass

class SimpleGraph:
    def __init__(self):
        self.edges: Dict[Location, List[Location]]={}
        
    def neighbors(self, id:Location)-> List[Location]:
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': [],
}

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, x: T):
        self.elements.append(x)
    
    def get(self) -> T:
        return self.elements.popleft()

from implementation import *

def breadth_first_search(graph: Graph, start: Location):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    reached: Dict[Location, bool] = {}
    reached[start] = True
    
    while not frontier.empty():
        current: Location = frontier.get()
        print("  Visiting %s" % current)
        for next in graph.neighbors(current):
            if next not in reached:
                frontier.put(next)
                reached[next] = True

print('Reachable from A:')
breadth_first_search(example_graph, 'A')
print('Reachable from E:')
breadth_first_search(example_graph, 'E')

    
