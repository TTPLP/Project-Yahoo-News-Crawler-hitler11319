import datetime

class News:
    def __init__(self, topic, author, date, test):

        #Let hr 2 digits, and if it is in the afternoon, then to plus 12 hours again
        if date.index(":") - date.index("午") == 2:
            date = date[0:14] + "0" + date[14:18]

        if date[12] == "下":
            date = date[0:14] + str(int(date[14:16])+12) + date[16:19]


        self.topic = topic
        self.author = author
        self.date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
        self.time = datetime.time(int(date[14:16]), int(date[17:18]), 0)
        self.test = test


    @property  
    def __str__(self):
        return "topic:{topic} \n author:{author} \n date:{date} \n test:{test} ".format(
            topic  =  self.topic,  
            author  =  self.author,  
            date  =  self.date,  
            test  =  self.test)

    @__str__.setter
    def __str__(self, topic, author, date, test):
        self.topic = topic
        self.author = author
        self.date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
        self.time = datetime.time(int(date[14:16]), int(date[17:18]), 0) 
        self.test = test 
