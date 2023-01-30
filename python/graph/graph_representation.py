from typing import Dict, List, Sequence


class Graph:
    """
    Representation of a graph as an adjacency list.
    """
    def __init__(self, adj_list: Dict = {}):
        self.adj_list = adj_list

    @classmethod
    def from_edge_list(cls, edge_list: List[Sequence[int]]):
        """
        Factory method to convert provided edge list into an adjacency list.
        Assuming each edge represents an edge from the first element to the second element.
        """
        graph = cls()
        for edge in edge_list:
            graph.add_edge(edge[0], edge[1])
        return graph

    def add_vertex(self, vertex: any):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, from_vertex: any, to_vertex: any, weight: int = 0):
        """
        Adds an edge from from_vertex to to_vertex.
        """
        if from_vertex not in self.adj_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adj_list:
            self.add_vertex(to_vertex)
        self.adj_list[from_vertex][to_vertex] = weight

    def neighbours(self, vertex: any) -> List:
        return list(self.adj_list[vertex].keys())

    def edge_weight(self, from_vertex: any, to_vertex: any):
        return self.adj_list[from_vertex][to_vertex]

    def get_vertices(self) -> List:
        return list(self.adj_list.keys())
