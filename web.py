import requests 
import re

url_list=[]    
class_list=[]

def dealstr(url):
    for y in url: #把html和"/取代為 + ,再把他分開字串（到時候要來取資料）
            y=y.replace("html"," + ",100).replace("\"/"," + ",100).split(" + ")  #弄出來的會是[[1,2],[2,3]]這種資料，所以下面會有2層


    for item in url: #這是把裡面的網址取出來（因為html被取代了！所以後面有.的是之前html所造成的）
        for it in range(0,len(item)):
            if item[it][-1]==".":
                url_list.append(item[it]) #符合的項目加入list[](這是網址的串列)


def againdeal(url,y):
	nextweb=requests.get("https://tw.news.yahoo.com/"+str(url)+"html")
	nextweb.encoding="utf-8"
	information=nextweb.text

	 #底下的str是因為list不能用replace函數，所以先轉
	topic=str(re.findall("<h1 class=\"headline\">.*</h1>",information))
	author=str(re.findall("<span class=\"provider org\">.*</span>",information))
	date=str(re.findall("<abbr title=.*</abbr>",information))
	test=str(re.findall("<p class=\"first\">.*</p>",information))


	topic=topic.replace("<h1 class=\"headline\">","").replace("</h1>","").replace("\\u3000","",20).replace("╱","",10) #\u3000是代表全形空白，而要取代時要變成\\才會有\出來！

	author=author.replace("<span class=\"provider org\">","").replace("</span>","")

	date=date.replace(">","<",10).split("<") #這比較麻煩，因為後面有會變的數，所以來分割（而其中第3項會是要的答案）
	date=date[2]

	test=test.replace("<p class=\"first\">","").replace("</p>","",100).replace(" ","",100).replace("<p>","",100)

	class_list[y]=news(topic,author,date,test) #將資料存進class
	print(class_list[y].__str__())

class news:
    def __init__(self,topic,author,date,test):
        self.topic=topic
        self.author=author
        self.date=date
        self.test=test
    def __str__(self):
    	return "topic:{topic} \n author:{author} \n date:{date} \n test:{test} ".format(
    		topic = self.topic, 
    		author = self.author, 
    		date = self.date, 
    		test = self.test)



firstweb=requests.get("https://tw.news.yahoo.com/society/")
firstweb.encoding="utf-8"
book=firstweb.text


m=re.findall('<a href=\"/.*html\" class=\"title \"',book) #把新聞弄出來


dealstr(m)

for url in list:
    againdeal(url,y)
    y+=1 #要讓y每次都加1（試過在def中他會一直跑y=0的式子）
        
