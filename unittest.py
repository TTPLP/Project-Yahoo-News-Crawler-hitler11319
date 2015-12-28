import unittest
import news

class News_mathod_test(unittest.TestCase):
    def setUp(self):
        self.news = news.List_news(["123", "456", "7839"])


    def test_append(self):
        test_input = "this is test input"
        self.assertEqual(self.news.append(test_input), ["123", "456", "7839", "this is test input"])

    def test_filter(self):
        goal = "3"
        self.assertEqual(self.news.filter(lambda item: goal in item),["123", "7839"])


if __name__ == '__main__':
    unittest.main()
