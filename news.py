
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
        return "topic:{topic} \n author:{author} \n date:{date} \n time:{time} \n text:{text} \n ".format(
            topic  =  self.topic,  
            author  =  self.author,  
            date  =  self.date,
            time = self.time,  
            text  =  self.text
        )

class List_news():
    def __init__(self):
        self.new = []

    def append(self, data):
        self.new.append(data)
        return self.new

    def len(self):
        return len(self.new)

    def search_author(self, goal):
        output = open(goal + ".txt", "wt")

        for y in self.new:
            if y.author == goal:
                output.write(y.__str__())

        output.close()

    def search_time(self, goal_date):

        import datetime
        import time

        if type(date) == datetime.date:

            before_time = open ("before " + str(date) + ".txt", "wt")
            after_time = open ("after " + str(date) + ".txt", "wt")

            for y in self.new:
                if time.mktime(goal_date.timetuple()) > time.mktime(y.date.timetuple()):
                    before_time.write(y.__str__())
                elif time.mktime(goal_date.timetuple()) < time.mktime(y.date.timetuple()):
                    after_time.write(y.__str__())

            before_time.close()
            after_time.close()
