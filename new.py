class news:
    def __init__(self, topic, author, date, test):
        self.topic = topic
        self.author = author
        self.date = date
        self.test = test
    def __str__(self):
        return "topic:{topic} \n author:{author} \n date:{date} \n test:{test} ".format(
            topic  =  self.topic,  
            author  =  self.author,  
            date  =  self.date,  
            test  =  self.test)