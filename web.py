import requests 
import re
import new

url_list = []
class_list = []

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


def againdeal(): 
    #deal with data, use append add to store_class , findally return
    store_class = []

    h1 = re.compile('<h1 class=\"headline\">.*</h1>')
    span = re.compile('<span class=\"provider org\">.*</span>')
    abbr = re.compile('<abbr title=.*</abbr>')
    p = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')        #It is very difficult thought for a long, but can be found with union

    for url in url_list:
       nextweb = requests.get('https://tw.news.yahoo.com/' + str(url) + 'html')
       nextweb.encoding = 'utf-8'
       information = nextweb.text

        #uer "str" ,  because list not use 
       topic = str(h1.findall(information)).replace('<h1 class=\"headline\">', '').replace('</h1>', '').replace('\\u3000', '', 20).replace('╱', '', 10)
       author = str(span.findall(information)).replace('<span class=\"provider org\">', '').replace('</span>', '')
       date = str(abbr.findall(information)).replace('>', '<', 10).split('<')[2]       #this is so trouble,  it is ["",  "<abbr title = ...",  "date",  "</abbr>",  ""],  so is data[2]
       test = str(p.findall(information)).replace('<p class=\"first\">', '').replace('</p>', '', 100).replace(' ', '', 100).replace('<p>', '', 100)

       store_class.append(new.news(topic, author, date, test))
    
    return store_class


if __name__ == '__main__':

    firstweb = requests.get('https://tw.news.yahoo.com/society/')
    firstweb.encoding = 'utf-8'
    book = firstweb.text


    m = re.findall('<a href=\"/.*html\" class=\"title \"', book) 

    url_list = dealstr(m)

    class_list = againdeal()



