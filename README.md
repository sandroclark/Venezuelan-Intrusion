# Venezuelan-Intrusion
by James Clark

## Analysis of Banned Venezuelan Twitter Accounts


# Table of Contents
- [Introduction](#Introduction)
- [Data Overview](#Data-Overview)
- [EDA](#EDA)
- [Data Pipeline](#Data-Pipeline)
- [Model-Selection](#Model-Selection)
- [Emotional Analysis](#Emotional-Analysis)
- [Wordclouds](#WordClouds)
- [Conclusion and Next Steps](#Conclusion-and-Next-Steps)


## Introduction
As machine learning takes the world by storm the negative consequences of adversarial machine learning more apparent. This project  utilizes Twitter's Dataset to examine the role and scope of Venezuelan interference in the '16 and '18 elections. 

#### Goal:
- Ascertain if Venezuela attempted to interfere in our elections.
- Understand the impact and nature of Venezuelan interference.
- Create visualizations to make impact better understood.
- Implement Sentiment Analysis on Tweets.
- Unsupervised Learning: Use LDA to derive latent topic. 
- Supervised Learning: Utilize classification Algorithms to identify how many actors are active in this campaign.


#### Motivation:
A major source of interest of mine is Political Science. I believe that High Tech can potentially make our society more Democratic, but also has the potential to undermine Democracies. By understanding these threats we can create greater protective measures to strengthen representative governments.

## Data Overview

#### First Dataset:
##### Twitter's Elections Integrity Dataset:
Collection of Tweets from Venezuelan accounts connected to state-sponsored disinformation campaigns.
- There are a half million tweets.
- Two Datasets: One dealing with tweets, the other with users.
- 33 Different Users.


#### Second Dataset:

##### [Emotions Sensor Data Set](https://www.kaggle.com/iwilldoit/emotions-sensor-data-set). 
- Contains over 21000 unique English words classified into 7 basic emotions: Disgust, Surprise, Neutral, Anger, Sad, Happy and Fear. 
- labeled using _Andbrain_(published on Kaggle) engine from over 1,185,540 classified words, blogs, tweets and sentences.



## EDA:

FEATURE ENGINEERING:

Follower Count of Handles(reach): Bar chart of how many followers these users had. They had some decent reach. With most accounts having over 1000 and just over 20 % having between upwards of 4k followers. (histogram)
(Insert histogram here)

FEATURE ENGINEERING:
How many tweets were viral: Defined viral as 100x more tweets than the median. Median was 1. out of half a million tweets 217 were classified as viral. With 4 tweets having over 1000 retweets.
(Insert histogram here)
EDA:

Although although the accounts language setting were spanish, the language in tweet body itself was overwhelmingly in English. With around 1/10 being in spanish. This is a radically different composition then the first twitter dataset release of Venezulean handles, which had majority of spanish tweets.
Thus opening up this data set to perform Sentiment Analysis.
(Insert histogram here)
TIME SERIES:

Tweets by day of Week: Not much variation, with slight decrease on weekends.

Other Time Series:

Huge spike of activity from mid '16 to 2nd quarter of '17. The spikes in this time period were 4x larger then the next spike around the midterms elections at the end of '18.
(insert time series here)
SENTIMENT ANALYSIS:

For sentiment analysis I used the emotion sensor dataset available on Kaggle. This dataset assigns sentiment to most popular 23k english words according to the the 7 basic emotions : Disgust, Surprise, Neutral, Anger, Sad, Happy and Fear. I used a counter of words in in tweets. Emotions in tweets by percentage : Fear 24 %, suprise 20 %, anger 23%. 
(insert graph here)


For Sentiment Analysis Series I used a count vector. With vocab being the emotion dataset, which I then fit the corpus of English Tweets that were not retweets. Then I made a df for each of the seven emotions setting index as tweet time and using Pandas built in to make this a date time object. I then plotted this df's by month.

During the peak tweeting periods the observable emotions are fear, surprise, anger.
(insert graph here)

## Data Pipeline
1.1.Words were lemmatized, stemmed. Punctuation removed. 
In linguistic morphology and information retrieval in **lemmatization** we are removing word endings to get to our target, the base or dictionary form of a word.  <br/>
Kittens - kitten, better - good, walking  - walk. <br/>

1.2. Stemming, the process of reducing inflected (or sometimes derived) words to their word stem, base or root form: <br/>
cats, catlike, and catty, cat ---> cat <br/>

`lemmer = WordNetLemmatizer()` <br/>

`stemmer = SnowballStemmer('english')` <br/>

1.3. Stop words. Noise. <br/>
Standard stop words library from nltk was used. <br/>
`stop_words = set(nltk.corpus.stopwords.words('english'))` <br/>

1.4 In addition the least meaningful words were arbitrary removed by the author using [**google trends**](https://trends.google.com/trends) and human comprehension. 
additional stopwords list (_developing_) in add_stop_words.py

1.5. Emojies, Urls, Hashtags and Mentions were out of scope of this research and removed from text using [Twitter text preprocessor](https://pypi.org/project/tweet-preprocessor/): </br>
`pip instal tweet-preprocessor`


# Model Selection:

The modeling methods I used were LDA and NMF. I utilized LDA four different ways: Simple Skilearn method, Grid search, Gensim, and LDA mallet. 

Using the Grid search method I found out the ideal amount of topics was 3 and a 1% learning decay.

Gensim LDA ideal topic amount was 5. 

NMF was used to see what I difference I would get in topics. It was different, with god showing up more in topics, and 'yuge' showing up.
(insert models here)

NOTES ON TUNING:

Coherence score without stemming only reached 56 %. Coherence Value with stemming was for most LDA methods was 43 %, except for LDA mallet which gave me a 1% increase to 57 %. From an inferential perspective topics were about the same (all political, all right wing, so I took out stemming). 

SUMMARY: 

SUMMARY OF DIFFERENT TOPICS:
All topics were Political. All were charged. Most mentioned Trump. Some models had god popping up more (NMF, it also had 'yuge' pop up). Hilary was also  in a lot of topics.

(insert word cloud) 
(insert best intertopic distance map here)

SUMMARY OF EMOTIONS/ TIME SERIES:

The emotions Venezuela wanted us to feel were overwhelmingly negative, with 60 % of the emotions being registered being Fear, Surprise, Anger. A huge tweet spike occurred in the last quartile of 2016. This spike corresponds to the to the election of '16. Another spike of activity occurred in 2018 in the beginning of year (primary season) and another around the midterm election. 


SUMMARY OF FEATURE ENGINEERING:

These accounts had decent reach with 20% of accounts having upwards of 4k followers. Although median retweet was value was 1, 217 tweets had 100x this amount of retweets and 4 having over 1k retweets.


# Conclusion and Next Steps

This project was really fun and informative for me because I was able to learn about Venezuelan interference on the side of Trump in the '16 election. This is information that is not widely known. After doing this project, I look at viral partisan posts in a different light, how many of likes on some of these posts are fake?

I'd love to continue using Data Science to explore topics relating politics.
