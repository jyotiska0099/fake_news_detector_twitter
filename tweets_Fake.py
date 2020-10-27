### Program to Scrape tweets to create Fake news Database
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

# User accounts on Twitter for genuine fake news
fakeNewsUser = 'PIBFactCheck'

### Create the Fake News Database
# Create Search String
t.Search = "from:@" + fakeNewsUser
print(t.Search)

# Creation of list that contains all tweets
twint.run.Search(t)
tweets = t.search_tweet_list

# Creation of dataframe from tweets list
tweets_1 = pd.DataFrame(tweets)
tweets_1 = tweets_1['tweet']

# Converting dataframe to CSV
print("[INFO]Saving to file...")
tweets_1.to_csv('database_fake.csv', sep=',')