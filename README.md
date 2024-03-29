# Venezuelan-Intrusion
by James Clark


# Table of Contents
- [Introduction](#Introduction)
- [Data Overview](#Data-Overview)
- [EDA](#EDA)
- [Data Pipeline](#Data-Pipeline)
- [Model-Selection](#Model-Selection)
- [Analysis of Tweets w/ Sentiment Analysis](#Analysis-of-Tweets-with-Sentiment-Analysis)
- [Conclusion and Next Steps](#Conclusion-and-Next-Steps)


## Introduction
The negative consequences of adversarial machine learning has become more apparent, with the recent interference into the U.S election by Russia. This project  utilizes Twitter's Dataset to examine the role and scope of Venezuelan interference in the '16 and '18 elections. 

#### Goal:
- Ascertain if Venezuela attempted to interfere in our elections.
- Understand the impact and nature of Venezuelan interference.
- Create visualizations to make impact better understood.
- Implement Sentiment Analysis on Tweets.
-  Use LDA to derive latent topics. 
- Utilize sentiment analysis on Tweets.
- Utilize classification Algorithms to identify how many actors are active in this campaign.


#### Motivation:
A passion of mine is Political Science. I believe that High Tech can potentially make our society more Democratic, but also has the potential to undermine Democracies. By understanding these threats we can create greater protective measures to strengthen representative governments.

<a href="#Venezuelan-Intrusion">Back to top</a>



## Data Overview

#### First Dataset:
##### Twitter's Elections Integrity Dataset:
[Twitter Election Integrity Data Set, Venezuela](https://about.twitter.com/en_us/values/elections-integrity.html#data)

Collection of Tweets from Venezuelan accounts connected to state-sponsored disinformation campaigns.
- There are a half million tweets.
- Two Datasets: One dealing with tweets, the other with users.
- 33 Different Users.


#### Second Dataset:

##### [Emotions Sensor Data Set](https://www.kaggle.com/iwilldoit/emotions-sensor-data-set) 
- Contains over 21000 unique English words classified into 7 basic emotions: Disgust, Surprise, Neutral, Anger, Sad, Happy and Fear. 
- Labeled using _Andbrain_(published on Kaggle) engine from over 1,185,540 classified words, blogs, tweets and sentences.

<a href="#Venezuelan-Intrusion">Back to top</a>

## EDA:


Performing EDA on the data set revealed a few things. They are summarized by the graphs below:

|Location of Users|
|:---:|
|![](img/Account_Locations.png)|

|All accounts registered as Spanish Language|Yet vast majority of actual Language in Tweets is English|
|:---:|:---:|
|![](img/Account_Language_fixed.png)|![](img/Language_in_Tweets_fixed.png)|

For further EDA please look at the summary [here](ExploratoryDataAnalysis.ipynb)


<a href="#Venezuelan-Intrusion">Back to top</a>

## Data Pipeline
1.1.Lemmatize and Stem Words. Remove punctuation. 
 
 **Lemmatizing** means removing word suffixes to get the base or dictionary form of a word.  <br/>
Kittens - kitten, better - good, walking  - walk. <br/>

 **Stemming** is the process of reducing words to their word stem, base or root form: <br/>
cats, catlike, and catty, cat ---> cat <br/>

`lemmer = WordNetLemmatizer()` <br/>

`stemmer = SnowballStemmer('english')` <br/>

1.3. Stop words. Noise. <br/>
Standard stop words library from nltk was used. <br/>
`stop_words = set(nltk.corpus.stopwords.words('english'))` <br/>

1.4. Emojies, Urls, Hashtags and Mentions removed from text using [Twitter text preprocessor](https://pypi.org/project/tweet-preprocessor/): </br>
`pip instal tweet-preprocessor`

The code to do this can be found [here](src/text_preprocessor_functions.py)


![](img/Nlp_Pipeline.png)

<a href="#Venezuelan-Intrusion">Back to top</a>
# Analysis of Tweets with Sentiment Analysis:

|Tweet Volume by 7 basic emotions| Tweet volume|
|:---:|:---:|
|![](img/7_basic_emotions_timeseries.png)|![](img/properly_labeled_timeseres.png)|

|Optimized number of Topics|Tweet Volume peaks during '16 Election|
|:---:|:---:|
|![](img/Emotions_Detected.png)|![](img/Tweet_Volume_Around_16_Election.png)|

## Results:

* A huge tweet spike occurred in the last quartile of 2016. This spike corresponds to  the election of '16.  
* Another spike of activity occurred in 2018 in the beginning of year (primary season) and another around the midterm election.

* It appears the tweet content of the banned accounts is mostly negative, with 60 % of the emotions counted as Fear, Surprise, Anger. 

For further Tweet Analysis please look at the summary [here](TweetAnalysis.ipynb)


<a href="#Venezuelan-Intrusion">Back to top</a>

# Model Selection:

**LDA is an unsupervised technique**, meaning that we don’t know prior to running the model **how many topics** exits in our corpus. **Coherence score** is a metric and main technique used to estimate the number of topics and to measure human understandability and interpretability.

|LDA using Gridsearch|LDA using Gensim|
|:---:|:---:|
|![](img/LDA_Sklearn.png)|![](img/LDA_Gensim.png)|

|Optimized number of Topics|
|:---:|
|![](img/optimal_coherence.png)|

The modeling methods I used were LDA and NMF. I utilized LDA four different ways: Simple Skilearn method, Grid search, Gensim, and LDA mallet. 

### Summary of LDA:
- Coherence score without stemming peaked at 56 %.
- Coherence score with stemming was 43 % using most methods.
- Except for LDA mallet which had highest coherence score of 57 %.


SUMMARY OF DIFFERENT TOPICS:
All topics were Political. All were charged. Most mentioned Trump. Some models had god popping up more (NMF, it also had 'yuge' pop up). Hilary was also  in a lot of topics.
![](img/3_topics.png)


The code for this can be found [here](Topic_Modeling.ipynb)

## Predicting Users
While exploring the Data I noticed many usernames were extremely similar. Such as: LaurenJonesGOP_ vs. LaurenJonesGOP , and DTrumpTrain_ vs. TrumpTrainNewss
I decided to use the following models to attempt to classify them based on tweets to see whether or not users were the same or not:

- Random Forest                
- Gradient Boosting Classifier 
- Naive Bayes Classifier                  
- Logistic Regression           
        
Random Forest and Gradient Boosting Classifiers (ensemble models) performed the best across the board. 

|Least Accurate Confusion Matrix @ 49 %|Most Accurate Confusion Matrix @ 64 %|
|:---:|:---:|
|![](img/NB_TrumpNComp.png)|![](img/Trump_Train_comp.png)|

One experiment betweeen 2 models named Trumpnews could not be classified with an accuracy greater than 50%, while two similarly named banned account called Trump Train could be accurately predicted with an accuracy up to 64%.

The code for this can be found [here](User_Predictor.ipynb)


<a href="#Venezuelan-Intrusion">Back to top</a>


# Conclusion and Next Steps

- Took the datasets and performed Exploratory Data Analysis
-  Using Sentiment analysis, Time stamps, and language of Corpus it can be inferred that Venezuela was targeting Americans.
- Built several models to classify different users 
- Next step would be to do more feature engineering such as: # of words, punctuation, and spelling to see if I can better predict how many different users were active in this misinformation campaign.


<a href="#Venezuelan-Intrusion">Back to top</a>
