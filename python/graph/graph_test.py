from graph_representation import Graph

edge_list = [(1, 2), (2, 3), (4, 1), (2, 4)]
vertices = [1, 2, 3, 4]


def test_graph_representation():
    graph = Graph.from_edge_list(edge_list)

    # Check vertices are added correctly
    verts = graph.get_vertices()
    for v in verts:
        assert v in vertices
    assert 100 not in verts

    # Check neighbours are correct
    neighbours_2 = graph.neighbours(2)
    assert sorted(neighbours_2) == [3, 4]

    neighbours_1 = graph.neighbours(1)
    assert neighbours_1 == [2]

    # Check add edge with weight is correct
    graph.add_edge(2, 1, 10)
    weight = graph.edge_weight(2, 1)
    assert weight == 10
