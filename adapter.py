from abc import ABC, abstractmethod

class AbstractGraph(ABC):
    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def add_edge(self, node1, node2):
        pass

    @abstractmethod
    def get_neighbors(self, node):
        pass

    @abstractmethod
    def get_nodes(self):
        pass

class Graph(AbstractGraph):
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        if node2 not in self.adjacency_list[node1] and node1 not in self.adjacency_list[node2]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)  

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def get_nodes(self):
        return list(self.adjacency_list.keys())