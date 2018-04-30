from nose.tools import assert_equal

class Node(object):
    def __init__(self, key):
        self.key = key
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {} # Key = Node, val = weight

    def add_neighbor(self, neighbor, weight=0):
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor] = weight
        neighbor.incoming_edges += 1

    def remove_neighbor(self, neighbor):
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor]
        neighbor.incoming_edges -= 1


class Graph(object):

    def __init__(self):
        """
        Keep track of all the nodes in the graph.
        Key is the node id and the associated value is the node object itself
        """
        self.nodes = {}

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node

    def add_edge(self, source, dest, weight=0):
        """
        Directed edges
        """
        self.nodes[source].add_neighbor(self.nodes[dest], weight)

    def add_undirected_edge(self, source, dest, weight=0):
        """
        Add undirected edges
        """
        self.nodes[source].add_neighbor(self.nodes[dest], weight)
        self.nodes[dest].adj_nodes[self.nodes[source].key] = self.nodes[source]
        self.nodes[dest].adj_weights[self.nodes[source]] = weight




if __name__ == '__main__':
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)

    print(graph.nodes)

    graph.add_edge(1, 2, 5)
    print(graph.nodes[1].adj_nodes)
    print(graph.nodes[1].adj_weights)



    #### TESTS for directed edges ####

    graph = Graph()
    for key in range(0, 6):
        graph.add_node(key)

    print(graph.nodes)

    graph.add_edge(0, 1, weight=5)
    graph.add_edge(0, 5, weight=2)
    graph.add_edge(1, 2, weight=3)
    graph.add_edge(2, 3, weight=4)
    graph.add_edge(3, 4, weight=5)
    graph.add_edge(3, 5, weight=6)
    graph.add_edge(4, 0, weight=7)
    graph.add_edge(5, 4, weight=8)
    graph.add_edge(5, 2, weight=9)

    print(graph.nodes[3].adj_nodes)
    print(graph.nodes[3].adj_weights)

    print(graph.nodes[0].incoming_edges)
    print(graph.nodes[1].incoming_edges)
    print(graph.nodes[2].incoming_edges)
    print(graph.nodes[3].incoming_edges)
    print(graph.nodes[4].incoming_edges)
    print(graph.nodes[5].incoming_edges)

    graph.nodes[0].remove_neighbor(graph.nodes[1])
    print(graph.nodes[1].incoming_edges)
    graph.nodes[3].remove_neighbor(graph.nodes[4])
    print(graph.nodes[4].incoming_edges)

    #### TESTS for undirected edges ####

    graph = Graph()
    for key in range(0, 6):
        graph.add_node(key)

    print(graph.nodes)

    graph.add_undirected_edge(0, 1, weight=5)
    graph.add_undirected_edge(0, 5, weight=2)
    graph.add_undirected_edge(1, 2, weight=3)

    print(graph.nodes[1].adj_nodes)
    print(graph.nodes[1].adj_weights)
