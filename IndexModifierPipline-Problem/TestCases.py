import unittest
from IndexModifierPipline import Node, Edge, Graph, connect_nodes

class TestGraphPipeline(unittest.TestCase):

    def test_simple_pipeline(self):
        node1 = Node(["cross", "square", "triangle", "circle"], None, None)
        edge1 = Edge(None, None, None)
        node2 = Node(["triangle", "circle", "cross", "square"], None, None)
        edge2 = Edge(None, None, None)
        node3 = Node(["circle", "cross", "square", "triangle"], None, None)
        edge3 = Edge(None, None, None)
        final_node = Node(["triangle", "cross", "circle", "square"], None, None)

        connect_nodes(node1, edge1, node2)
        connect_nodes(node2, edge2, node3)
        connect_nodes(node3, edge3, final_node)

        graph = Graph(node1)
        graph.topdown_fill_nodes()

        display_graph = graph.display_graph()
        print(display_graph)
        expected_output = """Displaying the graph:
            node: ['cross', 'square', 'triangle', 'circle']
                 Edges: (3, 4, 1, 2)
            node: ['triangle', 'circle', 'cross', 'square']
                 Edges: (2, 3, 4, 1)
            node: ['circle', 'cross', 'square', 'triangle']
                 Edges: (4, 2, 1, 3)
            Final node: ['triangle', 'cross', 'circle', 'square']
                    """

    def test_2(self):
        node1 = Node(["cross", "square", "triangle", "circle"], None, None)
        edge1 = Edge(None, None, [(3, 4, 1, 2),(4, 2, 1, 3)])
        node2 = Node(["triangle", "circle", "cross", "square"], None, None)
        edge2 = Edge(None, None, (2, 3, 4, 1))
        node3 = Node(["circle", "cross", "square", "triangle"], None, None)
        edge3 = Edge(None, None, (4, 2, 1, 3))
        final_node = Node(["triangle", "cross", "circle", "square"], None, None)

        connect_nodes(node1, edge1, node2)
        connect_nodes(node2, edge2, node3)
        connect_nodes(node3, edge3, final_node)

        graph = Graph(node1)
        graph.topdown_fill_nodes()

        display_graph = graph.display_graph()
        print(display_graph)
        expected_output = """Displaying the graph:
    node: ['cross', 'square', 'triangle', 'circle']
         Edges: (3, 4, 1, 2)
    node: ['triangle', 'circle', 'cross', 'square']
         Edges: (2, 3, 4, 1)
    node: ['circle', 'cross', 'square', 'triangle']
         Edges: (4, 2, 1, 3)
    Final node: ['triangle', 'cross', 'circle', 'square']
            """
        # self.assertEqual(display_graph, expected_output)
    # def test_three_nodes_pipeline(self):
    #     node1 = Node(["cross", "square", "triangle", "circle"], None, None)
    #     node2 = Node(["triangle", "circle", "cross", "square"], None, None)
    #     node3 = Node(["circle", "cross", "square", "triangle"], None, None)
    #     edge1 = Edge(node1, node2, (3, 4, 1, 2))
    #     edge2 = Edge(node2, node3, (4, 1, 2, 3))
    #     connect_nodes(node1, edge1, node2)
    #     connect_nodes(node2, edge2, node3)
    #     graph = Graph(node1)
    #     graph.topdown_fill_nodes()
    #     self.assertEqual(node3.data, ["circle", "cross", "square", "triangle"])
    #
    # def test_four_nodes_pipeline(self):
    #     node1 = Node(["cross", "square", "triangle", "circle"], None, None)
    #     node2 = Node(["circle", "cross", "square", "triangle"], None, None)
    #     node3 = Node(["square", "triangle", "circle", "cross"], None, None)
    #     node4 = Node(["triangle", "circle", "cross", "square"], None, None)
    #     edge1 = Edge(node1, node2, (4, 1, 2, 3))
    #     edge2 = Edge(node2, node3, (3, 4, 1, 2))
    #     edge3 = Edge(node3, node4, (2, 3, 4, 1))
    #     connect_nodes(node1, edge1, node2)
    #     connect_nodes(node2, edge2, node3)
    #     connect_nodes(node3, edge3, node4)
    #     graph = Graph(node1)
    #     graph.topdown_fill_nodes()
    #     self.assertEqual(node4.data, ["triangle", "circle", "cross", "square"])
    #
    # def test_five_nodes_pipeline(self):
    #     node1 = Node(["cross", "square", "triangle", "circle"], None, None)
    #     node2 = Node(["circle", "cross", "square", "triangle"], None, None)
    #     node3 = Node(["triangle", "circle", "cross", "square"], None, None)
    #     node4 = Node(["square", "triangle", "circle", "cross"], None, None)
    #     node5 = Node(["cross", "square", "triangle", "circle"], None, None)
    #     edge1 = Edge(node1, node2, (4, 1, 2, 3))
    #     edge2 = Edge(node2, node3, (3, 4, 1, 2))
    #     edge3 = Edge(node3, node4, (2, 3, 4, 1))
    #     edge4 = Edge(node4, node5, (1, 2, 3, 4))
    #     connect_nodes(node1, edge1, node2)
    #     connect_nodes(node2, edge2, node3)
    #     connect_nodes(node3, edge3, node4)
    #     connect_nodes(node4, edge4, node5)
    #     graph = Graph(node1)
    #     graph.topdown_fill_nodes()
    #     self.assertEqual(node5.data, ["cross", "square", "triangle", "circle"])

if __name__ == '__main__':
    unittest.main()