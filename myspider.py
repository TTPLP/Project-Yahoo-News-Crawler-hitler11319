from datetime import datetime, timedelta
import threading
import requests
import json
import re

class News:
    def __init__(self, topic, author, datetime, text):
        self.topic = topic
        self.author = author
        self.datetime = datetime
        self.text = text


    def __str__(self):
        return 'topic:{topic} , author:{author} , datetime:{datetime} , text:{text} '.format(
            topic  =  self.topic,  
            author  =  self.author,  
            datetime  =  self.datetime, 
            text  =  self.text
        )

    def toJson(self):
        return {'topic': self.topic, 'author': self.author, 'datetime': str(self.datetime), 'text': self.text}



class Spider:
    def __init__(self, first_url):
        self.first_url = first_url
        self.channels = []
        self.url_list = []
        self.data = []

    def add_channel(self, channel):
        return self.channels.append(channel)

    def crawl(self, url):
        information = requests.get(url)
        information.encoding = 'utf-8'
        return information.text

    def crawl_link(self, url):
        data = self.crawl(url)
        link = re.findall('<a href=\"/.*html\" class=\"title \"', data)

        # as Yahoo_news_crawler/crawler.py dealstr() same 
        for y in range(0, len(link)): 
            link[y] = link[y].replace('html', ' + ', 100).replace('\"/', ' + ', 100).split(' + ')  


        for item in link: 
            for it in range(0, len(item)):
                if item[it][-1] == '.':
                    self.url_list.append(item[it])

        return self.url_list

    def crawl_data(self, url):
        topic_split = re.compile('<h1 class=\"headline\">.*</h1>')
        author_split = re.compile('<span class=\"provider org\">.*</span>')
        date_split = re.compile('<abbr title=.*</abbr>')
        text_split = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')

        data = self.crawl(self.first_url + str(url) + 'html')

        try:
            #uer "str" ,  because list not use 
            topic = str(topic_split.findall(data)).replace('<h1 class=\"headline\">', '').replace('</h1>', '').replace('\\u3000', '', 20).replace('╱', '', 10).replace('[', '', 10).replace(']', '',10)
            author = str(author_split.findall(data)).replace('<span class=\"provider org\">', '').replace('</span>', '').replace('[', '', 10).replace(']', '',10)
            date = str(date_split.findall(data)).replace('>', '<', 10).split('<')[2]      #this is so trouble,  it is ["",  "<abbr title = ...",  "date",  "</abbr>",  ""],  so is data[2]
            text = str(text_split.findall(data)).replace('<p class=\"first\">', '').replace('</p>', '', 100).replace(' ', '', 100).replace('<p>', '', 100).replace('[', '', 10).replace(']', '',10).replace('\',\'', '', 10)

            #deal with date
            if '下' in date:
                date = date.replace('下午', '')
                try:
                    date = datetime.strptime(date, '%Y年%m月%d日 %H:%M') + timedelta(hours = 12)
                except:
                    date = datetime.strptime(date, '%Y年%m月%d日 %H:%M') + timedelta(days = 1, hours = -12)
            else:
                date = date.replace('上午', '')
                date = datetime.strptime(date, '%Y年%m月%d日 %H:%M') 


            self.data.append(News(topic, author, date, text).toJson())

            print('第', len(self.data), '則新聞已擷取完')
        except:
            pass

    def save(self, data):
        with open('items.json', 'wt', encoding = 'utf-8') as output:
            output.write(data)

    def start(self):
        for channel in self.channels:
            self.crawl_link(channel)

        for url in self.url_list:
            thread = threading.Thread(target = self.crawl_data, args = (url, ))
            thread.start()

        #until thread.start() end , run
        thread.join()
        self.save(json.dumps(self.data, ensure_ascii = False))

            
        

        

    

        

        

    

    
