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

    def fitler(self):
        pass

    def fitler(self):
        pass
