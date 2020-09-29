# Import necessary packages
from absl import logging
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import pandas as pd
import re

# Load the model
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"  # @param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model = hub.load(module_url)
print("module %s loaded" % module_url)


def embed(input):
    return model(input)


# Load the csv files
fake_news_df = pd.read_csv("database_fake.csv")
true_news_df = pd.read_csv("database_true.csv")
collected_news_df = pd.read_csv("database_collected.csv")

# Cleaning data
def clean_data(x):
    text = x
    text = text.lower()
    text = re.sub("\[.*?\]", "", text)  # remove square brackets
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub("\w*\d\w*", "", text)  # remove words containing numbers
    text = re.sub(r"http\S+", "", text)
    text = re.sub("\n", "", text)
    return text


### Check for verified fake news
verified_fake = []
yet_to_check = []
for i in range(len(collected_news_df)):
    found = 0
    # Get message1 from collected data
    msg1 = collected_news_df.iloc[i][1]
    msg1 = clean_data(msg1)

    for j in range(len(fake_news_df)):
        # Get message2 from verified fake data
        msg2 = fake_news_df.iloc[j][1]
        msg2 = clean_data(msg2)
        messages = [msg1, msg2]
        # Reduce logging output.
        logging.set_verbosity(logging.ERROR)
        # Embed the messages
        message_embeddings = embed(messages)
        # Find Corelation
        features = message_embeddings
        corr = np.inner(features, features)
        # Check for similarity
        if corr[0][1] >= 0.95:
            found = 1
            break

    if found == 1:
        verified_fake.append(msg1)
    else:
        yet_to_check.append(msg1)


### Check for verified true news
probably_fake = []
for i in range(len(yet_to_check)):
    found = 0
    # Get message 1 from yet_to_check
    msg1 = yet_to_check[i]
    msg1 = clean_data(msg1)

    for j in range(len(true_news_df)):
        # Get message2 from verified true data
        msg2 = true_news_df.iloc[j][1]
        msg2 = clean_data(msg2)
        messages = [msg1, msg2]
        # Reduce logging output.
        logging.set_verbosity(logging.ERROR)
        # Embed the messages
        message_embeddings = embed(messages)
        # Find Corelation
        features = message_embeddings
        corr = np.inner(features, features)
        # Check for similarity
        if corr[0][1] >= 0.95:
            found = 1
            break

    if found == 0:
        probably_fake.append(msg1)


# The tweets in Probably fake are for further check either manual or using a ML model
# Store the Probably Fake
fake = pd.DataFrame(probably_fake, )

# Converting dataframe to CSV
fake.to_csv('database_probable.csv', sep=',')