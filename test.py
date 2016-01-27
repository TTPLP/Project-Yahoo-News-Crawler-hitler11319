from datetime import datetime
import unittest
import os

import news
import crawler


class News_mathod_test(unittest.TestCase):
    def setUp(self):
        self.news = news.List_news()  

        self.news.append(news.News('hello', 'me', datetime(2015, 10, 5, 12, 50, 0), 'hello you are '))
        self.news.append(news.News('ok', 'you', datetime(2015, 12, 18, 18, 25, 0), 'are you ok' ))

    def test_append(self):
        self.news.append(news.News('a', 'a', datetime(1000, 6, 18, 1, 25, 0), 'a'))
        
        self.assertEqual(len(self.news), 3)

    def test_filter(self):
        goal = "ok"
        
        for i in self.news.filter(lambda item: goal in item.text):
            self.assertIn("ok", i.topic)

    def test_dealstr(self):
        url = ["<a href=\"/405964.html class=\"hello\"  ", "<a href=\"/66482.html class=\"hello\"", "<a href=\"/11158.html class=\"hello\""]
        self.assertEqual(crawler.dealstr(url), ["405964.", "66482.", "11158."])

    def test_search_author(self):
        goal = 'me'

        for item in self.news.search_author(goal):
            self.assertIn('me', item.author)

    def test_search_time(self):
        first_goal_time = 16
        end_goal_time = 20

        for item in self.news.search_time(first_goal_time, end_goal_time):
            self.assertIn('ok', item.text)

    def test_search_topic(self):
        keyword = 'he'

        for item in self.news.search_topic(keyword):
            self.assertIn('hello', item.topic)

    def test_againdeal(self):
        base_url = 'https://tw.news.yahoo.com/'
        url_list = ['123']

        with open('t.json', "wt", encoding = 'utf-8') as output:
            crawler.againdeal(url_list, output, base_url)
        
        with open('t.json', "rt", encoding = 'utf-8') as result:
            self.assertEqual(len(result.read()), 0)

        os.remove('t.json')


if __name__ == '__main__':
    unittest.main()
