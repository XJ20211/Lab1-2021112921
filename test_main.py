import unittest
# 这里替换为你自己的模块名
import main

class TestQueryBridgeWordsMethod(unittest.TestCase):

    # setUp方法在每个测试方法执行前被调用
    def setUp(self):
        text = "book apple fruit bananas table"
        self.graph = main.create_directed_graph(text)

    # 测试用例1
    def test_case_1(self):
        self.assertEqual(main.query_bridge_words(self.graph, "apple", "bananas"), "The bridge words from apple to bananas are: fruit.")
        result = main.query_bridge_words(self.graph, "apple", "bananas")
        print("实际输出：", result)

    # 测试用例2
    def test_case_2(self):
        self.assertEqual(main.query_bridge_words(self.graph, "book", "table"), "No bridge words from book to table!")
        result = main.query_bridge_words(self.graph, "book", "table")
        print("实际输出：", result)

    # 测试用例3
    def test_case_3(self):
        self.assertEqual(main.query_bridge_words(self.graph, "book", "banana"), "No book or banana in the graph!")
        result = main.query_bridge_words(self.graph, "book", "banana")
        print("实际输出：", result)

    # 测试用例4
    def test_case_4(self):
        self.assertEqual(main.query_bridge_words(self.graph, "", "bananas"), "No  or bananas in the graph!")
        result = main.query_bridge_words(self.graph, "", "bananas")
        print("实际输出：", result)

    # 测试用例5
    def test_case_5(self):
        self.assertEqual(main.query_bridge_words(self.graph, "apple123", "bananas"), "No apple123 or bananas in the graph!")
        result = main.query_bridge_words(self.graph, "apple123", "bananas")
        print("实际输出：", result)

    # 测试用例6
    def test_case_6(self):
        self.assertEqual(main.query_bridge_words(self.graph, "test", "test"), "No test or test in the graph!")
        result = main.query_bridge_words(self.graph, "test", "test")
        print("实际输出：", result)

if __name__ == '__main__':
    unittest.main()
