
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

    def save(self, items, output):
        i = 1
        for item in items:
            output.write(str(item))
            print("第" + str(i) + "則已讀取")
            i += 1

        print("讀取完畢")

    def filter(self, func):
        for item in self.news:
            if func(item): yield item   #self.filter() is list( so save only 1 floor)

    def search_author(self, goal):
        output = open(goal + ".json", "wt")
        
        self.save(self.filter(lambda item: goal in item.author), output)

        output.close()

    def search_time(self, first_goal_time, end_goal_time):

        import datetime

        output = open(str(first_goal_time) + " \n o'clock to " + str(end_goal_time) + "\n o'clcok news.json", "wt")

        self.save(self.filter(lambda item: first_goal_time <= item.time.hour < end_goal_time), output)

        output.close()

    def search_topic(self, keyword):
        output = open("about" + keyword + "news.json", "wt")

        self.save(self.filter(lambda item: keyword in item.topic), output)

        output.close()

