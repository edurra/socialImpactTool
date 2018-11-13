from tweetsRetriever import Twitter
from newsRetriever import News

word = "Ferrari"
ndays = 3

#twitter api params
twitter_requests_per_day = 3
tweets_per_request = 100
new_file_twitter = "PATH_TO_FILE"

#news api params
news_request_per_day = 1
page_size = 100
new_file_news = "PATH_TO_FILE"

twitter = Twitter(word = word, requests_per_day= twitter_requests_per_day, tweets_per_request= tweets_per_request, ndays=ndays, filename=new_file_twitter)
news = News(word = word, page_size= page_size, filename = new_file_news, ndays = ndays, requests_per_day= news_request_per_day)

twitter.createCSV()
news.createCSV()
