from tweetsRetriever import Twitter
from newsRetriever import News
import os

word = "Microsoft"
ndays = 7

#twitter api params
twitter_requests_per_day = 1
tweets_per_request = 100
new_file_twitter = "/home/maria_dev/tempTweets.csv"

#news api params
news_request_per_day = 1
page_size = 100
new_file_news = "/home/maria_dev/tempNews.csv"

twitter = Twitter(word = word, requests_per_day= twitter_requests_per_day, tweets_per_request= tweets_per_request, ndays=ndays, filename=new_file_twitter)
news = News(word = word, page_size= page_size, filename = new_file_news, ndays = ndays, requests_per_day= news_request_per_day)

twitter.createCSV()
os.system('hadoop fs -ls copyFromLocal tempTweets.csv /user/maria_dev')
os.system('spark-submit --master yarn --deploy-mode cluster XXXXXX.py')
news.createCSV()
os.system('hadoop fs -ls copyFromLocal tempNews.csv /user/maria_dev')
os.system('spark-submit --master yarn --deploy-mode cluster XXXXXX.py')

os.system('rm /home/maria_dev/tempTweets.csv')