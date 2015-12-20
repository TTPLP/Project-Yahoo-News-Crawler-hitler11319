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
    if date.index("月") - date.index("年") ==2:
        date = date[0:5] + "0" + date[5:] 

    if date.index("日") - date.index("月") ==2:
        date = date[0:8] + "0" + date[8:]

    if date.index(":") - date.index("午") == 2:
        date = date[0:14] + "0" + date[14:]

    if date[12] == "下":
        if date[14:16] == "12":
            date = date[0:14] + "00" + date[16:19]
        else:
            date = date[0:14] + str(int(date[14:16])+12) + date[16:19]

    return date


def againdeal(url_list, output): 
    #deal with data, use append add to store_class , findally return
    store_class = news.List_news()
    i = 0

    h1 = re.compile('<h1 class=\"headline\">.*</h1>')
    span = re.compile('<span class=\"provider org\">.*</span>')
    abbr = re.compile('<abbr title=.*</abbr>')
    p = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')        #It is very difficult thought for a long, but can be found with union

    for url in url_list:
        
        i += 1

        nextweb = requests.get('https://tw.news.yahoo.com/' + str(url) + 'html')
        nextweb.encoding = 'utf-8'
        information = nextweb.text

        #uer "str" ,  because list not use 
        topic = str(h1.findall(information)).replace('<h1 class=\"headline\">', '').replace('</h1>', '').replace('\\u3000', '', 20).replace('╱', '', 10)
        author = str(span.findall(information)).replace('<span class=\"provider org\">', '').replace('</span>', '')
        date = str(abbr.findall(information)).replace('>', '<', 10).split('<')[2]       #this is so trouble,  it is ["",  "<abbr title = ...",  "date",  "</abbr>",  ""],  so is data[2]
        text = str(p.findall(information)).replace('<p class=\"first\">', '').replace('</p>', '', 100).replace(' ', '', 100).replace('<p>', '', 100)

        date = change_time_format(date)

        store_class.append(news.News(topic, author, date[0:11], date[14:], text))

        #The results are output in the js file and outputs the captured Ikunori News
        output.write(store_class.new[i - 1].__str__())
        print("第", i, "則新聞已擷取完，還剩下", len(url_list) - i, "則新聞")
        if i  == len(url_list) : print("已擷取完畢！")
    
    return store_class

def main():
    url_list = []
    class_list = []

    firstweb = requests.get('https://tw.news.yahoo.com/society/')
    firstweb.encoding = 'utf-8'
    book = firstweb.text


    m = re.findall('<a href=\"/.*html\" class=\"title \"', book) 

    url_list = dealstr(m)

    output = open("result.json", "wt")

    class_list = againdeal(url_list, output)

    output.close()

if __name__ == '__main__':
    main()

