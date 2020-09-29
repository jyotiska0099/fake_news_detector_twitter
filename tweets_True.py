### Program to Scrape tweets to create True news Database
# git clone --branch=twitter_legacy2 https://github.com/yunusemrecatalcam/twint.git 
# Install twint from only the above modified branch

# Import Necessary Packages
import twint
import csv
import pandas as pd
import nest_asyncio
nest_asyncio.apply()

# Initialise Twint
t = twint.Config()
t.Store_object = True
# Number of crawling
t.Limit = 10

# User accounts on Twitter for genuine news
trueNewsUsers = ['PIB_India', 'ANI', 'EduMinOfIndia', 'MoHFW_INDIA']

### Create the True News Database
tweets = []
for user in trueNewsUsers:
	# Create Search String
	t.Search = "from:@" + user
	print(t.Search)

	# Creation of list that contains all tweets
	twint.run.Search(t)
	tweets.extend(t.search_tweet_list)

# Creation of dataframe from tweets list
tweets_2 = pd.DataFrame(tweets)
tweets_2 = tweets_2['tweet']

# Converting dataframe to CSV
tweets_2.to_csv('database_true.csv', sep=',')
