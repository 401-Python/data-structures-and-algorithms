import pytest

from graph import Graph, Vertex

def test_add_node():
    
    graph = Graph()

    expected = 'spam' # a vertex's value that comes back

    actual = graph.add_node('spam').value

    assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():
    
    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)




def test_add_edge_interloper_end():
    
    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_groovy():
    
    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)

# nosy, get rid of once public method available
def test_add_edge_effect():

    graph = Graph()

    end = graph.add_node('banana')

    start = graph.add_node('apple')

    graph.add_edge(start, end)

    expected = (end, 0)

    actual = graph._adjacency_list[start][0]

    assert actual == expected

# nosy, get rid of once public method available
def test_add_edge_effect_with_weight():

    graph = Graph()

    end = graph.add_node('banana')

    start = graph.add_node('apple')

    graph.add_edge(start, end, 44)

    expected = (end, 44)

    actual = graph._adjacency_list[start][0]

    assert actual == expected


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())
    
    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    # expect collection, weights included

    neighbors = graph.get_neighbors(apple)

    # expected = # a list, 1 long, with tuple of (<'banana'>,44)


    assert len(neighbors) == 1

    assert neighbors[0][0].value == 'banana'

    assert isinstance(neighbors[0][0], Vertex)

    assert neighbors[0][1] == 44






    



