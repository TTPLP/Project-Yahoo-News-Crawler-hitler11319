import myspider

if __name__ == '__main__':
    target = myspider.Spider('https://tw.news.yahoo.com/')
    
    myspider.Channel().add_channel('https://tw.news.yahoo.com/society/')
    myspider.Channel().add_channel('https://tw.news.yahoo.com/sports/')
    myspider.Channel().add_channel('https://tw.news.yahoo.com/entertainment/')
    
    target.start()


