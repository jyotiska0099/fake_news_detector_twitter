### Program to Scrape tweets to check 
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
t.Limit = 100

## Collecting tweets based on a #tag
# Create Search String; In our case, chage the string to "from:@trueOrFake4" from "monkey"
t.Search = 'monkey'
print("from:#"+t.Search)

# Creation of list that contains all tweets
twint.run.Search(t)
tweets = t.search_tweet_list

# Creation of dataframe from tweets list
tweets_3 = pd.DataFrame(tweets)
tweets_3 = tweets_3['tweet']

# Converting dataframe to CSV
print("[INFO]Saving to file...")
tweets_3.to_csv('database_collected.csv', sep=',')