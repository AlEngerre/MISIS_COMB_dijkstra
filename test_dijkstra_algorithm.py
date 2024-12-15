import unittest
from dijkstra_algorithm import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 6},
            'C': {'A': 4, 'B': 2, 'D': 3},
            'D': {'B': 6, 'C': 3}
        }
        result = dijkstra(graph, 'A')
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 6}
        self.assertEqual(result, expected)

    def test_single_vertex(self):
        graph = {'A': {}}
        result = dijkstra(graph, 'A')
        expected = {'A': 0}
        self.assertEqual(result, expected)

    def test_disconnected_graph(self):
        graph = {
            'A': {'B': 2},
            'B': {'A': 2},
            'C': {}
        }
        result = dijkstra(graph, 'A')
        expected = {'A': 0, 'B': 2, 'C': float('inf')}
        self.assertEqual(result, expected)

    def test_negative_weights(self):
        graph = {
            'A': {'B': 1},
            'B': {'C': -2},
            'C': {}
        }
        with self.assertRaises(ValueError):
            dijkstra(graph, 'A')

if __name__ == "__main__":
    unittest.main()
