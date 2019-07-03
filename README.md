# Venezuelan-Intrusion
Analysis and Topic Modeling of Banned Venezuelan Twitter Accounts
(Draft)

1. High Level Description of Project(motivation,goals,etc):

For the past 5 years as Data Science has taken the world by storm I gained appreciation for Data Science as analytical tool in Political Science. My 'meta' goal for this project was to to use modeling techniques such as LDA and NMF as well NLP to interpret something of importance in our Democracy, in this case that is utilization of twitter as means of affecting public mood and perception. Twitter releases datasets of banned accounts and my goal was for this project was to peform EDA,Modeling,Sentiment Analysis infer what Venezuela's intentions were, who they were they supporting, where were they tweeting from, and the reach of their tweets.

2. EDA:

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
3.

MODELING:

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

CONTEXT OF THIS DATASET WITH PREVIOUS VENEZUELA DATASET:

This dataset was had less spanish tweets, and its locations were predominantly stated to be in the States. It can thus be inferred that these accounts were not for a domestic targets like previous dataset. The tweets were quite clearly targeting Americans. All topics were right political in nature and right wing and mostly 'negative'. The peak tweet volume occurred precisely in early november. It is quite surprising that both Venezuela and Russia were taking part in the same activities on the same side. It is however curious to me that the tweets supported Trump so much, since Trump is no friend of Maduro's govt. It leads me to think that Maduro didn't think Trump was much of a threat, and is instead sought to gin up American division by propping up toxic right wing ideology. 

FINAL THOUGHTS/FUTURE WORK:

This project was really fun and informative for me because I was able to learn about Venezuelan interference on the side of Trump in the '16 election. This is information that is not widely known. After doing this project, I look at viral partisan posts in a different light, how many of likes on some of these posts are fake?

I'd love to continue using Data Science to explore topics relating politics.
