import pytrends
from datetime import datetime, timedelta
from pytrends.request import TrendReq


pytrend = TrendReq()
substracted_days = 6

now = datetime.now()
past_date = now - timedelta(days = substracted_days)

year_now = str(now.year)
month_now = str(now.month)
day_now = str(now.day)

year_substracted = str(past_date.year)
month_substracted = str(past_date.month)
day_substracted = str(past_date.day)

timeframe = year_substracted+"-"+month_substracted+"-"+day_substracted+" "+year_now+"-"+month_now+"-"+day_now

word = "Comcast"

kwlist=[word]

pytrend.build_payload(kwlist, timeframe=timeframe)

#Dictionary
related_queries = pytrend.related_queries().items()
#Pandas dataframe
print related_queries[0][1]['top']

#Pandas dataframe
interest = pytrend.interest_over_time()
print interest