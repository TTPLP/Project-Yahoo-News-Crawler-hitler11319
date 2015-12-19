
class News:
    def __init__(self, topic, author, date, time, text):
        import datetime

        self.topic = topic
        self.author = author
        self.date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
        self.time = datetime.time(int(time[0:2]), int(time[3:]), 0)
        self.text = text


    def __str__(self):
        return "topic:{topic} \n author:{author} \n date:{date} \n time:{time} \n text:{text} ".format(
            topic  =  self.topic,  
            author  =  self.author,  
            date  =  self.date,
            time = self.time,  
            text  =  self.text
        )


