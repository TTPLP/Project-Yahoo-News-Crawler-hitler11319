from datetime import datetime
import requests 
import re

import news


def dealstr(url):
    get_url = []
    # this is use "html" and " "/  " to split the str ,  let me gain the url(ps:but get the data is[[1, 2], [2, 3]] ,  so have 2 floor )
    for y in range(0, len(url)): 
        url[y] = url[y].replace('html', ' + ', 100).replace('\"/', ' + ', 100).split(' + ')  

    # get the url ,  because it have 2 floor , so use 2 for. And get the url store in url_list
    for item in url: 
        for it in range(0, len(item)):
            if item[it][-1] == '.':
                get_url.append(item[it])

    return get_url


def change_time_format(date):
    #Let hr and month and day have 2 digits, and if it is in the afternoon, then to plus 12 hours again
    if date.index("月") - date.index("年") == 2:
        date = date[0:5] + "0" + date[5:] 

    if date.index("日") - date.index("月") == 2:
        date = date[0:8] + "0" + date[8:]

    if date.index(":") - date.index("午") == 2:
        date = date[0:14] + "0" + date[14:]

    if date[12] == "下":
        if date[14:16] == "12":
            date = date[0:14] + "00" + date[16:19]
        else:
            date = date[0:14] + str(int(date[14:16])+12) + date[16:19]

    return date


def againdeal(url_list, output, base_url): 
    #deal with data, use append add to store_class , findally return
    store_class = news.List_news()

    i = 1

    topic_split = re.compile('<h1 class=\"headline\">.*</h1>')
    author_split = re.compile('<span class=\"provider org\">.*</span>')
    date_split = re.compile('<abbr title=.*</abbr>')
    text_split = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')        #It is very difficult thought for a long, but can be found with union

    for url in url_list:

        nextweb = requests.get(base_url + str(url) + 'html')
        nextweb.encoding = 'utf-8'
        information = nextweb.text

        #Prevent coding problems
        try:
            #uer "str" ,  because list not use 
            topic = str(topic_split.findall(information)).replace('<h1 class=\"headline\">', '').replace('</h1>', '').replace('\\u3000', '', 20).replace('╱', '', 10)
            author = str(author_split.findall(information)).replace('<span class=\"provider org\">', '').replace('</span>', '')
            date = str(date_split.findall(information)).replace('>', '<', 10).split('<')[2]       #this is so trouble,  it is ["",  "<abbr title = ...",  "date",  "</abbr>",  ""],  so is data[2]
            text = str(text_split.findall(information)).replace('<p class=\"first\">', '').replace('</p>', '', 100).replace(' ', '', 100).replace('<p>', '', 100)

            date = change_time_format(date)


            store_class.append(news.News(topic, author, datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[14:16]), int(date[17:]), 0), text))

            #The results are output in the js file and outputs the captured Ikunori News
            output.write(str(i) + "  " +str(store_class.news[i - 1]))
            print("第", i, "則新聞已擷取完")
            i += 1
        except:
            continue
  
    print("讀取完畢！")

    return store_class

def using_keyword(class_list):
    keyword = input("請輸入關鍵字：")

    result = class_list.search_topic(keyword)

    store_or_print(result)

def using_time(class_list):
    first_goal_time = int(input("請輸入時段的開題（0-23)："))
    end_goal_time = int(input("請輸入時段的結尾（1-24)："))

    result = class_list.search_time(first_goal_time, end_goal_time)

    store_or_print(result)

def using_author(class_list):
    goal = input("請輸入作者：")

    result = class_list.search_author(goal)

    store_or_print(result)

def leave(class_list):
    print('謝謝使用！')
    exit()

def error(class_list):
    print("ERROR")

# use user to choose store or print
def store_or_print(result):

    def save(data):
        with open(input("請輸入檔名:")+".json", "wt", encoding = 'utf-8') as output:
            for item in data:
                output.write(str(item))
        
    def output(data):
        for item in data:
            print(str(item))

    def error(result):
        print('error')

    func_dict = {"S":save, "O":output}
    print("\n S.儲存\n O.輸出")
    func_dict.get(input("輸入指令（注意是大寫）:"), error)(result)

def main():
    url_list = []          #put into first web url list
    class_list = []        #every web data stroe in class and retrun it as list
    base_url = 'https://tw.news.yahoo.com/'   #this is yahoo news head url
    function_dict = {"1":using_keyword, "2":using_time, "3":using_author, "4":leave}

    firstweb = requests.get('https://tw.news.yahoo.com/society/')
    firstweb.encoding = 'utf-8'
    book = firstweb.text


    m = re.findall('<a href=\"/.*html\" class=\"title \"', book)    #m is search all urs list 

    url_list = dealstr(m)

    output = open("result.json", "wt", encoding = 'utf-8')

    class_list = againdeal(url_list, output, base_url)

    output.close()

    while True:
        print( " \n 1.找標題\n 2.找一段時間 \n 3.找作者 \n 4.離開")

        function_dict.get(input("請輸入數字："), error)(class_list)


if __name__ == '__main__':
    main()


