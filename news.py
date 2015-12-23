
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
        output = open(goal + ".json", "wt")

        count = 0

        for y in self.new:
            if y.author == goal:
                output.write(y.__str__())
                print("第", count, "則新聞已讀取")
                count += 1

        if count != 0:
            print("讀取完畢")
        else:
            print("查無此資料")


        output.close()

    def search_time(self, first_goal_time, end_goal_time):

        import datetime

        output = open(first_goal_time + "點到" + end_goal_time + "點的新聞.json", "wt")

        count = 0

        for y in self.new:
            if first_goal_time <= y.time.hour < end_goal_time:
                output.wiite(y.__str__())
                print("第", count, "則新聞已讀取")
                count += 1

        if count != 0:
            print("讀取完畢")
        else:
            print("查無此資料")

        output.close()

    def search_topic(self, keyword):
        output = open("有關", keyword, "的新聞.json", "wt")

        count =0

        for y in self.new:
            if keyword in y.topic:
                output.write(y.__str__())
                print("第", count, "則新聞已讀取")
                count += 1

        if count != 0:
            print("讀取完畢")
        else:
            print("查無此資料")

        output.close()
