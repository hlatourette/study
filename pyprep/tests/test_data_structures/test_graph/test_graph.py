import unittest

from data_structures.graph.graph import Graph


class TestStack(unittest.TestCase):
    def setUp(self):
        graph_adj_list = {
            0: [1, 2, 3],
            1: [4, 5],
            2: [5],
            3: [6],
            4: [6],
            5: [7],
            6: [6]
        }
        digraph_adj_list = {
            0: [1, 2, 3],
            1: [0, 4, 5],
            2: [5],
            3: [0, 6],
            4: [1, 6],
            5: [7],
            6: [],
            7: [7]
        }
        multigraph_adj_list = {
            0: [1, 2, 3],
            1: [0, 4, 5, 7],
            2: [5, 5],
            3: [6],
            4: [6],
            5: [1, 2, 7],
            6: [6, 6]
        }
        multidigraph_adj_list = {
            0: [1, 1, 2, 3],
            1: [0, 4, 5],
            2: [5],
            3: [6],
            4: [1, 6, 6],
            5: [7],
            6: [],
            7: [7, 7]
        }
        self.graph = Graph(graph_adj_list, directed=False, multigraph=False)
        self.digraph = Graph(digraph_adj_list, directed=True, multigraph=False)
        self.multigraph = Graph(multigraph_adj_list, directed=False, multigraph=True)
        self.multidigraph = Graph(multidigraph_adj_list, directed=True, multigraph=True)

    def test_construct_graph(self):
        self.assertEqual(sorted(self.graph[0]), [1, 2, 3])
        self.assertEqual(sorted(self.graph[1]), [0, 4, 5])
        self.assertEqual(sorted(self.graph[2]), [0, 5])
        self.assertEqual(sorted(self.graph[3]), [0, 6])
        self.assertEqual(sorted(self.graph[4]), [1, 6])
        self.assertEqual(sorted(self.graph[5]), [1, 2, 7])
        self.assertEqual(sorted(self.graph[6]), [3, 4, 6])
        self.assertEqual(sorted(self.graph[7]), [5])

    def test_construct_digraph(self):
        self.assertEqual(sorted(self.digraph[0]), [1, 2, 3])
        self.assertEqual(sorted(self.digraph[1]), [0, 4, 5])
        self.assertEqual(sorted(self.digraph[2]), [5])
        self.assertEqual(sorted(self.digraph[3]), [0, 6])
        self.assertEqual(sorted(self.digraph[4]), [1, 6])
        self.assertEqual(sorted(self.digraph[5]), [7])
        self.assertEqual(sorted(self.digraph[6]), [])
        self.assertEqual(sorted(self.digraph[7]), [7])

    def test_construct_multigraph(self):
        self.assertEqual(sorted(self.multigraph[0]), [1, 1, 2, 3])
        self.assertEqual(sorted(self.multigraph[1]), [0, 0, 4, 5, 5, 7])
        self.assertEqual(sorted(self.multigraph[2]), [0, 5, 5, 5])
        self.assertEqual(sorted(self.multigraph[3]), [0, 6])
        self.assertEqual(sorted(self.multigraph[4]), [1, 6])
        self.assertEqual(sorted(self.multigraph[5]), [1, 1, 2, 2, 2, 7])
        self.assertEqual(sorted(self.multigraph[6]), [3, 4, 6, 6])
        self.assertEqual(sorted(self.multigraph[7]), [1, 5])

    def test_construct_multidigraph(self):
        self.assertEqual(sorted(self.multidigraph[0]), [1, 1, 2, 3])
        self.assertEqual(sorted(self.multidigraph[1]), [0, 4, 5])
        self.assertEqual(sorted(self.multidigraph[2]), [5])
        self.assertEqual(sorted(self.multidigraph[3]), [6])
        self.assertEqual(sorted(self.multidigraph[4]), [1, 6, 6])
        self.assertEqual(sorted(self.multidigraph[5]), [7])
        self.assertEqual(sorted(self.multidigraph[6]), [])
        self.assertEqual(sorted(self.multidigraph[7]), [7, 7])

    def test_add_edge_graph(self):
        self.graph.add_edge(2, 3)
        self.assertEqual(sorted(self.graph[2]), [0, 3, 5])
        self.assertEqual(sorted(self.graph[3]), [0, 2, 6])
    
    def test_add_edge_digraph(self):
        self.digraph.add_edge(2, 3)
        self.assertEqual(sorted(self.digraph[2]), [3, 5])
        self.assertEqual(sorted(self.digraph[3]), [0, 6])
        
    def test_add_edge_multigraph(self):
        self.multigraph.add_edge(2, 3)
        self.multigraph.add_edge(2, 3)
        self.assertEqual(sorted(self.multigraph[2]), [0, 3, 3, 5, 5, 5])
        self.assertEqual(sorted(self.multigraph[3]), [0, 2, 2, 6])

    def test_add_edge_multidigraph(self):
        self.multidigraph.add_edge(2, 3)
        self.multidigraph.add_edge(2, 3)
        self.assertEqual(sorted(self.multidigraph[2]), [3, 3, 5])
        self.assertEqual(sorted(self.multidigraph[3]), [6])

    def test_add_edge_existing_graph(self):
        self.assertRaises(Exception, self.graph.add_edge, 0, 1)
        self.assertRaises(Exception, self.graph.add_edge, 1, 0)

    def test_add_edge_existing_digraph(self):
        self.assertRaises(Exception, self.digraph.add_edge, 0, 1)

    def test_add_edge_existing_multigraph(self):
        self.multigraph.add_edge(0, 1)
        self.assertEqual(sorted(self.multigraph[0]), [1, 1, 1, 2, 3])
        self.assertEqual(sorted(self.multigraph[1]), [0, 0, 0, 4, 5, 5, 7])

    def test_add_edge_existing_multidigraph(self):
        self.multidigraph.add_edge(0, 1)
        self.assertEqual(sorted(self.multidigraph[0]), [1, 1, 1, 2, 3])
        self.assertEqual(sorted(self.multidigraph[1]), [0, 4, 5])

    def test_add_edge_loop_graph(self):
        self.graph.add_edge(0, 0)
        self.assertEqual(sorted(self.graph[0]), [0, 1, 2, 3])
    
    def test_add_edge_loop_digraph(self):
        self.digraph.add_edge(0, 0)
        self.assertEqual(sorted(self.digraph[0]), [0, 1, 2, 3])
    
    def test_add_edge_loop_multigraph(self):
        self.multigraph.add_edge(0, 0)
        self.multigraph.add_edge(6, 6)
        self.assertEqual(sorted(self.multigraph[0]), [0, 1, 1, 2, 3])
        self.assertEqual(sorted(self.multigraph[6]), [3, 4, 6, 6, 6])

    def test_add_edge_loop_multidigraph(self):
        self.multidigraph.add_edge(6, 6)
        self.multidigraph.add_edge(7, 7)
        self.assertEqual(sorted(self.multidigraph[6]), [6])
        self.assertEqual(sorted(self.multidigraph[7]), [7, 7, 7])

    def test_add_edge_new_u_vertex_graph(self):
        self.graph.add_edge(8, 0)
        self.assertEqual(sorted(self.graph[0]), [1, 2, 3, 8])
        self.assertEqual(sorted(self.graph[8]), [0])

    def test_add_edge_new_u_vertex_digraph(self):
        self.digraph.add_edge(8, 0)
        self.assertEqual(sorted(self.digraph[0]), [1, 2, 3])
        self.assertEqual(sorted(self.digraph[8]), [0])

    def test_add_edge_new_u_vertex_multigraph(self):
        self.multigraph.add_edge(8, 0)
        self.assertEqual(sorted(self.multigraph[0]), [1, 1, 2, 3, 8])
        self.assertEqual(sorted(self.multigraph[8]), [0])

    def test_add_edge_new_u_vertex_multidigraph(self):
        self.multidigraph.add_edge(8, 0)
        self.assertEqual(sorted(self.multidigraph[0]), [1, 1, 2, 3])
        self.assertEqual(sorted(self.multidigraph[8]), [0])

    def test_add_edge_new_v_vertex_graph(self):
        self.graph.add_edge(0, 8)
        self.assertEqual(sorted(self.graph[0]), [1, 2, 3, 8])
        self.assertEqual(sorted(self.graph[8]), [0])

    def test_add_edge_new_v_vertex_digraph(self):
        self.digraph.add_edge(0, 8)
        self.assertEqual(sorted(self.digraph[0]), [1, 2, 3, 8])
        self.assertEqual(sorted(self.digraph[8]), [])
    
    def test_add_edge_new_v_vertex_multigraph(self):
        self.multigraph.add_edge(0, 8)
        self.assertEqual(sorted(self.multigraph[0]), [1, 1, 2, 3, 8])
        self.assertEqual(sorted(self.multigraph[8]), [0])
    
    def test_add_edge_new_v_vertex_multidigraph(self):
        self.multidigraph.add_edge(0, 8)
        self.assertEqual(sorted(self.multidigraph[0]), [1, 1, 2, 3, 8])
        self.assertEqual(sorted(self.multidigraph[8]), [])

    def test_add_edges_graph(self):
        self.graph.add_edges(adj_list={0:[4]}, edge_list=[(2, 3)])
        self.assertEqual(sorted(self.graph[0]), [1, 2, 3, 4])
        self.assertEqual(sorted(self.graph[2]), [0, 3, 5])
        self.assertEqual(sorted(self.graph[3]), [0, 2, 6])
        self.assertEqual(sorted(self.graph[4]), [0, 1, 6])

    def test_size_of(self):
        self.assertEqual(len(self.graph), 8)
        self.assertEqual(len(self.digraph), 8)
        self.assertEqual(len(self.multigraph), 8)
        self.assertEqual(len(self.multidigraph), 8)

    def test_delete_vertex_graph(self):
        del self.graph[0]
        self.assertRaises(KeyError, self.graph.__getitem__, 0)
        self.assertEqual(sorted(self.graph[1]), [4, 5])
        self.assertEqual(sorted(self.graph[2]), [5])
        self.assertEqual(sorted(self.graph[3]), [6])

    def test_delete_vertex_digraph(self):
        del self.digraph[0]
        self.assertRaises(KeyError, self.digraph.__getitem__, 0)
        self.assertEqual(sorted(self.digraph[1]), [4, 5])
        self.assertEqual(sorted(self.digraph[3]), [6])

    def test_delete_vertex_multigraph(self):
        del self.multigraph[0]
        self.assertRaises(KeyError, self.multigraph.__getitem__, 0)
        self.assertEqual(sorted(self.multigraph[1]), [4, 5, 5, 7])
        self.assertEqual(sorted(self.multigraph[2]), [5, 5, 5])
        self.assertEqual(sorted(self.multigraph[3]), [6])

    def test_delete_vertex_multidigraph(self):
        del self.multidigraph[0]
        self.assertRaises(KeyError, self.multidigraph.__getitem__, 0)
        self.assertEqual(sorted(self.multidigraph[1]), [4, 5])

    def test_delete_missing_vertex_graph(self):
        self.assertRaises(KeyError, self.graph.__delitem__, 8)

    def test_delete_missing_vertex_digraph(self):
        self.assertRaises(KeyError, self.digraph.__delitem__, 8)

    def test_delete_missing_vertex_multigraph(self):
        self.assertRaises(KeyError, self.multigraph.__delitem__, 8)

    def test_delete_missing_vertex_multidigraph(self):
        self.assertRaises(KeyError, self.multidigraph.__delitem__, 8)