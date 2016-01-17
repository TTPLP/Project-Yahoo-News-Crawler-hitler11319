from datetime import datetime


class News:
    def __init__(self, topic, author, datetime, text):

        self.topic = topic
        self.author = author
        self.datetime = datetime
        self.text = text


    def __str__(self):
        return "topic:{topic} \n author:{author} \n datetime:{datetime} \n text:{text} \n \n".format(
            topic  =  self.topic,  
            author  =  self.author,  
            datetime  =  self.datetime, 
            text  =  self.text
        )

class List_news():
    def __init__(self, default = None):

        if default is None:
            self.news = []
        else:
            self.news = default

    def append(self, data):
        #data must not be None, so use try ... except deal with 
        if  type(data) == News :
            self.news.append(data)
            return self.news
        else:
            raise BaseException

    def __len__(self):
        return len(self.news)

    def __iter__(self):
        return self

    def __next__(self):

        i = -1

        if i < len(self.news):
            i +=1
            return self.news[i]


    def filter(self, func):
        for item in self.news:
            if func(item): yield item   #self.filter() is list( so save only 1 floor)

    def search_author(self, goal):
        
        return self.filter(lambda item: goal in item.author)

    def search_time(self, first_goal_time, end_goal_time):

        return self.filter(lambda item: first_goal_time <= item.datetime.hour < end_goal_time)


    def search_topic(self, keyword):

        return self.filter(lambda item: keyword in item.topic)




