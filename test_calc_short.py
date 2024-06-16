import unittest
import networkx as nx
import main

class TestCalcShortestPath(unittest.TestCase):

    def setUp(self):
        text = "book apple fruit bananas table"
        self.graph = main.create_directed_graph(text)

    def test_case1(self):
        expected = "Shortest path: apple -> fruit -> bananas with total weight 2"
        result = main.calc_shortest_path(self.graph, "apple", "bananas")
        self.assertEqual(result, expected)
        print("实际输出：", result)

    def test_case2(self):
        expected = "Shortest path to apple: apple with total weight 0\nShortest path to fruit: apple -> fruit with total weight 1\nShortest path to bananas: apple -> fruit -> bananas with total weight 2\nShortest path to table: apple -> fruit -> bananas -> table with total weight 3"
        result = main.calc_shortest_path(self.graph, "apple")
        self.assertEqual(result, expected)
        print("实际输出：", result)

    def test_case3(self):
        expected = "No path available."
        result = main.calc_shortest_path(self.graph, "apple", "book")
        self.assertEqual(result, expected)
        print("实际输出：", result)

    def test_case4(self):
        expected = "nonexistent not in the graph!"
        result = main.calc_shortest_path(self.graph, "nonexistent")
        self.assertEqual(result, expected)
        print("实际输出：", result)

if __name__ == "__main__":
    unittest.main()
