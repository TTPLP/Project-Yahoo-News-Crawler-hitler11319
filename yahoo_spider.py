import myspider

if __name__ == '__main__':
    target = myspider.Spider('https://tw.news.yahoo.com/')
    target.add_channel('https://tw.news.yahoo.com/society/')
    target.start()
