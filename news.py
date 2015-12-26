
class News:
    def __init__(self, topic, author, date, time, text):

        import datetime

        if type(date) == datetime.date and type(time) == datetime.time :
            self.topic = topic
            self.author = author
            self.date = date
            self.time = time
            self.text = text


    def __str__(self):
        return "topic:{topic} \n author:{author} \n date:{date} \n time:{time} \n text:{text} \n  \n".format(
            topic  =  self.topic,  
            author  =  self.author,  
            date  =  self.date,
            time = self.time,  
            text  =  self.text
        )

class List_news():
    def __init__(self):
        self.news = []

    def append(self, data):
        self.news.append(data)
        return self.news

    def len(self):
        return len(self.news)

    def filter(self, func, output):
        for item in self.news:
            if func(item): output.write(str(item))

    def search_author(self, goal):
        output = open(goal + ".json", "wt")
        
        self.filter(lambda item: item.author == goal, output)

        output.close()

    def search_time(self, first_goal_time, end_goal_time):

        import datetime

        output = open(first_goal_time + "o'clock to " + end_goal_time + "o'clcok news.json", "wt")

        self.filter(lambda item: first_goal_time <= item.time.hour < end_goal_time, output)

        output.close()

    def search_topic(self, keyword):
        output = open("about" + keyword + "news.json", "wt")

        self.filter(lambda item: keyword in item.topic, output)

        output.close()
