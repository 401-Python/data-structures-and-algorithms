import collections

class Graph:

    def __init__(self):

        self._adjacency_list = {}

    
    def add_node(self, value):
        """adds a vertex
        
        Arguments:
            value {[value]} -- [description]
        
        Returns:
            vertex
        """
        v = Vertex(value)

        self._adjacency_list[v] = []

        return v


    def size(self):
        return len(self._adjacency_list)


    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append((end_vertex,weight))


    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]
    

class Vertex:
    def __init__(self, value):
        self.value = value







g = Graph()
one = g.add_node('1')
two = g.add_node('2')
three = g.add_node('3')
four = g.add_node('4')
five = g.add_node('5')

g.add_edge(one, two, 12)
g.add_edge(two, three, 23)
g.add_edge(three, four, 34)
g.add_edge(four, five, 45)
g.add_edge(five, one, 51)

