import unittest
import news
import web
import datetime

class News_mathod_test(unittest.TestCase):
    def setUp(self):
        self.news = news.List_news()

        self.news.append(news.News('hello', 'me', datetime.date(2015, 10, 5), datetime.time(12, 50, 0), 'hello you are '))
        self.news.append(news.News('ok', 'you', datetime.date(2015, 12, 18), datetime.time(18, 25, 0), 'are you ok '))

    def test_append(self):
        test_input = "this is test input"
        self.assertEqual(len(self.news.append(test_input)), 3)

    def test_save(self):
        items = ['hello', 'ok']

        output = open('t.json', "wt")
        self.news.save(items, output)
        output.close()

        result = open('t.json', "rt").read()
        self.assertEqual(result, 'hellook')

    def test_filter(self):
        total = ""
        goal = "ok"
        for i in self.news.filter(lambda item: goal in item.text):
            total += i.topic
        self.assertEqual(total, "ok")

    def test_change_time_format(self):
        date = "2015年12月20日 下午3:12"
        self.assertEqual(web.change_time_format(date), "2015年12月20日 下午15:12")

    def test_dealstr(self):
        url = ["<a href=\"/405964.html class=\"hello\"  ", "<a href=\"/66482.html class=\"hello\"", "<a href=\"/11158.html class=\"hello\""]
        self.assertEqual(web.dealstr(url), ["405964.", "66482.", "11158."])

    def test_search_author(self):
        goal = 'me'

        self.news.search_author(goal)

        result = open('me.json', "rt").read()

        self.assertEqual(len(result), 84)

    def test_search_time(self):
        first_goal_time = 16
        end_goal_time = 20

        self.news.search_time(first_goal_time, end_goal_time)

        result = open('16  o\'clock to 20  o\'clcok news.json', "rt").read()

        self.assertEqual(len(result), 79)

    def test_search_topic(self):
        keyword = 'he'

        self.news.search_topic(keyword)

        result = open('about he news.json', "rt").read()

        self.assertEqual(len(result), 84)

if __name__ == '__main__':
    unittest.main()
