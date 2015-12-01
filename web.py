import requests #爬第一個主頁的網
firstweb=requests.get("https://tw.news.yahoo.com/society/")
firstweb.encoding="utf-8"
book=firstweb.text

list=[] #存網址
new={} #將內容存在字典
import re
m=re.findall('<a href=\"/.*html\" class=\"title \"',book) #把新聞弄出來


def dealstr(x):
    for y in range(0,len(x)): #把html和"/取代為 + ,再把他分開字串（到時候要來取資料）
            x[y]=x[y].replace("html"," + ",100)
            x[y]=x[y].replace("\"/"," + ",100)
            x[y]=x[y].split(" + ") #弄出來的會是[[1,2],[2,3]]這種資料，所以下面會有2層

    for item in x: #這是把裡面的網址取出來（因為html被取代了！所以後面有.的是之前html所造成的）
        for it in range(0,len(item)):
            if item[it][-1]==".":
                list.append(item[it]) #符合的項目加入list[](這是網址的串列)

dealstr(m)
try_list=[number for number in range(0,len(list))] #這是要用來存class的，裡面內容放數字，反正用完後內容也是無法用的
y=0 #這是用來當引數來存進class的，所以底下會每次加1

def againdeal(x,y):
	import requests #爬分頁的網
	nextweb=requests.get("https://tw.news.yahoo.com/"+str(x)+"html")
	nextweb.encoding="utf-8"
	information=nextweb.text

	import re #底下的str是因為list不能用replace函數，所以先轉
	g=str(re.findall("<h1 class=\"headline\">.*</h1>",information))
	r=str(re.findall("<span class=\"provider org\">.*</span>",information))
	t=str(re.findall("<abbr title=.*</abbr>",information))
	s=str(re.findall("<p class=\"first\">.*</p>",information))
	g=g.replace("<h1 class=\"headline\">","")
	g=g.replace("</h1>","")
	g=g.replacce("\\u3000","",20) #\u3000是代表全形空白，而要取代時要變成\\才會有\出來！
	r=r.replace("<span class=\"provider org\">","")
	r=r.replace("</span>","")
	t=t.replace(">","<",10) #這比較麻煩，因為後面有會變的數，所以來分割（而其中第3項會是要的答案）
	t=t.split("<")
	t=t[2]
	s=s.replace("<p class=\"first\">","")
	s=s.replace("</p>","",100)
	s=s.replace(" ","",100)
	s=s.replace("<p>","",100)
	
	e={g:{"作者":r , "日期":t , "內文":s}} #將內容化為字典
	new.update(e)

	try_list[y]=news(g,r,t,s) #將資料存進class

	
for i in list:
    y+=1 #要讓y每次都加1（試過在def中他會一直跑y=0的式子）
    againdeal(i,y)
        

class news:
        def __init__(self,topic,writer,date,test):
                self.topic=topic
                self.writer=writer
                self.date=date
                self.test=test