# fake_news_detector_twitter

	This is an entry for the competition "Innovation for Assam" organised by Assam Police. By the Team "hawkeyes". This prototype scrape tweets from some verified and genuine accounts to create a database of true news. we are planning to start our own twitter handle as "fakeOrNot". People will post different tweets which are seem fake by taging us. Those tweets then be scraped to store in a separate database. A sentence similarity algorithm checks for any possible match. If a collected news is declared as fake after 3 level of checking it will be posted on our official handle as a verified fake news.


# Requirements

	Install the following python libraries
		1. tensorflow
		2. tensorflow_hub
		3. pandas
		4. numpy
		5. absl-py
		6. os
		7. re
		8. twint (Install only from "git clone --branch=twitter_legacy2 https://github.com/yunusemrecatalcam/twint.git" )
		9. nest_asyncio
		10. csv


# Steps to follow

	## Step1: Prepare the databases
	1. Run "python tweets_Fake.py" to collect the already verified fake news
	2. Run "python tweets_True.py" to collect the genuine true news
	3. Run "python tweets_collect.py" to collect the news to be checked

	## Step2: Comparison
	1. Run "python comparison.py" to compare the collected news to existing genuine news. Here we are using Google's Universal Sentence Encoder's TF Hub module to perform the lexical as well as semantic similarity.

# Three Level of Comparison
	
	Level 1: 
	Compare the collected news with already verified fake news

	Level 2: 
	Those which does not have any match in level 1, compare them with genuine true news

	Level 3:
	Those which pass level 2 and no match found, they are further checked manually or using a pre-trained Machine Learning model. The development codes for the model are given in the notebook "trueOrFake.ipynb". The datasets used are given in "datasets" folder.

# Additional Notes.
	* The '.csv' file generated will be stored in the same directory
	* The "Sentence_similarity_hackathon_AP.ipynb" notebook is given here to show the efficiency of the comparison algorithm.