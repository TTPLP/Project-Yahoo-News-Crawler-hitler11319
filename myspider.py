from datetime import datetime, timedelta

import time
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
            topic = self.topic,  
            author = self.author,  
            datetime = self.datetime, 
            text = self.text
        )

    def toDict(self):
        return {'topic': self.topic, 'author': self.author, 'datetime': str(self.datetime), 'text': self.text}



class Spider:
    def __init__(self, first_url):
        self.first_url = first_url

    def crawl(self, url):
        information = requests.get(url)
        information.encoding = 'utf-8'
        return information.text

    def save(self, data):
        with open('items.json', 'wt', encoding = 'utf-8') as output:
            output.write(json.dumps(data, ensure_ascii = False))

    def start(self):
        rlock = threading.RLock()

        for channel in Channel().channels:
            rlock.acquire()
            thread = threading.Thread(target = Channel().crawl, args = (channel, self.first_url, ))
            thread.start()
            rlock.release()

class Channel(Spider):
    def __init__(self, channel = []):
        self.channels = channel
        
    def add_channel(self, channel_list):
        return self.channels.append(channel_list)

    def crawl(self, url, first_url):
        store = []    #use to store the channel each item url(already try: use threading , 3 store have own data, so not repeat)
        
        data = super().crawl(url)
        link = re.findall('<a href=\"/.*html\" class=\"title \"', data)

        # as Yahoo_news_crawler/crawler.py dealstr() same 
        for y in range(0, len(link)): 
            link[y] = link[y].replace('html', ' + ').replace('\"/', ' + ').split(' + ')  

        for item in link: 
            for it in range(0, len(item)):
                if item[it][-1] == '.':
                    Page().append_url(item[it])
                    store.append(item[it])



        #every channel have own crawl url data
        rlock = threading.RLock()
        for items in store:
            rlock.acquire()
            thread1 = threading.Thread(target = Page().crawl, args = (items, first_url, ))
            thread1.start()
            rlock.release()
            

        return Page().url_list

    def get_all(self):
        return self.channels

    def __len__(self):
        return len(self.channels)


class Page(Spider):
    def __init__(self, url_list = [], data = []):
        self.url_list = url_list
        self.data = data
        
    def crawl(self, url, first_url):
        topic_split = re.compile('<h1 class=\"headline\">.*</h1>')
        author_split = re.compile('<span class=\"provider org\">.*</span>')
        date_split = re.compile('<abbr title=.*</abbr>')
        text_split = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')

        url_data = super().crawl(first_url + str(url) + 'html')

        try:
            #uer "str" ,  because list not use 
            topic = str(topic_split.findall(url_data)).replace('<h1 class=\"headline\">', '').replace('</h1>', '').replace('\\u3000', '', 20).replace('╱', '', 10).replace('[', '', 10).replace(']', '',10)
            author = str(author_split.findall(url_data)).replace('<span class=\"provider org\">', '').replace('</span>', '').replace('[', '', 10).replace(']', '',10)
            date = str(date_split.findall(url_data)).replace('>', '<', 10).split('<')[2]      #this is so trouble,  it is ["",  "<abbr title = ...",  "date",  "</abbr>",  ""],  so is data[2]
            text = str(text_split.findall(url_data)).replace('<p class=\"first\">', '').replace('</p>', '', 100).replace(' ', '', 100).replace('<p>', '', 100).replace('[', '', 10).replace(']', '',10).replace('\',\'', '', 10)

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


            self.data.append(News(topic, author, date, text).toDict())

            print('第', len(self.data), '則新聞已擷取完')
            
            #certain threading is over
            if len(self.url_list) == len(self.data):
                print('資料擷取完畢')
                super().save(self.data)
        except:
            self.url_list.remove(url)   #let self.url_list long as same as self.data, so if not have data del it.
            raise UnicodeEncodeError


    def __len__(self):
        return len(self.data)

    def append_url(self, obj):
        return self.url_list.append(obj)

               
