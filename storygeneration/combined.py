import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random
import os 
import subprocess
from subprocess import call

from .sample import sample

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]
   
stop_words = stopwords.words('english')
   
positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []
   
for tokens in positive_tweet_tokens:
    positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))
   
for tokens in negative_tweet_tokens:
    negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))
   
all_pos_words = get_all_words(positive_cleaned_tokens_list)
   
freq_dist_pos = FreqDist(all_pos_words)
   
positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
   
positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]
   
negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]
   
dataset = positive_dataset + negative_dataset
   
random.shuffle(dataset)
   
train_data = dataset[:7000]
test_data = dataset[7000:]
   
classifier = NaiveBayesClassifier.train(train_data)
    
#storygen

def checkSent(out, sentToken):
    custom_tweet = out
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    sent=classifier.classify(dict([token, True] for token in custom_tokens))
    if sent == sentToken:
        return 1
    else:
        return 0

def storyGen(sentToken1,sentToken2,prompt):
	ip1=prompt
	if sentToken1=='No' and sentToken2=='No':
		flag = 1
	else:
		flag = 0

	bad_chars = ['  ', '\n', '\r'] 

	while(True):

		if flag==0:
			out = sample(['--prime',str(ip1),'--quiet'])
		else:
			out = sample(['--prime',str(ip1),'--pick','2','--quiet'])

		out=out.strip()

		return(out)
		
		if flag==1:
			#print(out, flush="True")
			break
		else:
			flag2=checkSent(out, sentToken1)
			if flag2==1:
				#print(out, flush="True")
				break

	out1=str(out).split('.')
	ip2=out1[-1]
	ip2=ip2.strip('"')
	ip2=ip2.strip()
	ip2=out1[-1]
	ip3=out1[-2]
	ip2=ip3+ip2

def generateStory(theme, prompt):
	if theme=='Mystery':
		sentToken1='Negative'
		sentToken2='Positive'
	elif theme=='Thriller':
		sentToken1='Positive'
		sentToken2='Negative'
	elif theme=='Happy':
		sentToken1='Positive'
		sentToken2='Positive'
	elif theme=='Tragedy':
		sentToken1='Negative'
		sentToken2='Negative'
	elif theme=='Default':
		sentToken1='No'
		sentToken2='No'
	result = storyGen(sentToken1,sentToken2, prompt)
	return(result)
