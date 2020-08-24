# Description
This are the scrips generated for the project "Development of a social impact assesment tool". The idea was to create a PoC for atool that allows companies to analyze their social impact, understanding social impact as the reactions of people on social networks, as well as the reactions of the media to the actions carried out by a company.

# Scripts
**TweetsRetriever.py** Used to access the Twitter API (via [Tweepy](https://www.tweepy.org/) ) and get tweets containing the name of the company

**TweetsProcessing.py** Processes the retrieved tweets with pyspark and sends the results to the mysql database

**NewsRetriever.py** Retrieves news containing the name of the company ( [NewsAPI](https://newsapi.org/) )

**NewsProcessing.py** Processes the retrieved news with pyspark and sends the results to the mysql database

**TrainModel.py** Trains a machine learning model using Spark MLLib and stores it on a local file

**TrendsRetriever.py** Retrieves useful information about the company from [Google Trends](https://trends.google.es/trends/)
