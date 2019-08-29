### Creating a function to clean_up the twitter_text

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

#Additional
import string
string.punctuation

# In this edit I didn't remove # and @ hoping to find the way to remove it together with the followings
punct = set(string.punctuation)
punct.remove('@')
punct.remove('#')






lemmer = WordNetLemmatizer()
stemmer = SnowballStemmer('english')


### STOP WORDS --  combining w/custom list of most frequently used and uninformative words (see news_stop_words)
stop_words = set(nltk.corpus.stopwords.words('english')) 

### I HAVE THIS INSIDE THE FUNCTION AS WELL, NEED TO TEST IF WORKS IF REMOVE FROM HERE
new_stop_words = {'rt', 'hey' 'via', 'new', 'time', 'today', 'one', 'say', 'get', 'go', 
                  'im', 'know', 'need', 'made', 'https', 'http', 'that', 'would', 
                  'take', 'your', 'two', 'yes', 'back', 'look', 'see', 'amp', 'tell',
                  'give', 'httpst', 'htt', 'use', 'dont', 'thing', 'man', 'thank', 'lol', 'cc', 'agre' }

import preprocessor as p
import re

def preprocessing_text(text):
    '''
    INPUT: str
    OUTPUT: str w/ emojies, urls, hashtags and mentions removed
    '''
    p.set_options(p.OPT.EMOJI, p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.NUMBER, p.OPT.RESERVED, p.OPT.SMILEY)
    clean_text = p.clean(text)
    
    return clean_text

def remove_symbols(word, symbol_set):
    
    '''
    Removing symbols from word
    '''
    return ''.join(char for char in word 
                    if char not in symbol_set)

def clean_tweet_text(text_column):
    '''
    takes a columns in dataframe with tweets text: 
    Outputs: PD Series of tokenized docs
    lower case, 
    symbol_set charachters removed,
    specified stop words removed
    punctuation removed
    words stemmed and lemmatized
    
    '''
    
    
    # converting from pd to list
    corpus = text_column.values.tolist()
    
    #Removing all HTTPs
    docs_no_http = [ re.sub(r'https?:\/\/.*\/\w*', '', doc) for doc in corpus ]
    #First ---> tokenize docs
    tokenized_docs = [doc.split() for doc in docs_no_http]
    # Lower case words in doc
    tokenized_docs_lowered  = [[word.lower() for word in doc]
                                for doc in tokenized_docs]

    # Removing punctuation from docs
    cleaned_docs = [[remove_symbols(word, punct) for word in doc] 
                    for doc in tokenized_docs_lowered]

    ### Removing stop words
#     stop_words = set(nltk.corpus.stopwords.words('english'))


    stop_words = set(nltk.corpus.stopwords.words('english'))

    new_stop_words = {'rt', 'via', 'new', 'time', 'today', 'one', 'say', 'get', 'go', 
                      'im', 'know', 'need', 'made', 'https', 'http', 'that', 'would', 
                      'take', 'your', 'two', 'yes', 'back', 'look', 'see', 'amp', 'tell',
                      'give', 'httpst', 'htt', 'use', 'dont', 'thing', 'man', 'thank'}

    
    docs_no_stops1 = [[word for word in doc if word not in new_stop_words] 
                     for doc in cleaned_docs]
    
    docs_no_stops = [[word for word in doc if word not in stop_words ] 
                     for doc in docs_no_stops1]
    # Lemmatize words in docs
    docs_lemmatized = [[lemmer.lemmatize(word) for word in doc]
                      for doc in docs_no_stops]
    
#     # Stem words in docs
#     docs_stemmed = [[stemmer.stem(word) for word in doc]
#                       for doc in docs_lemmatized]
    
    # Removes mentions, emotions, hashtags and emojies
    docs_no_mentions = [preprocessing_text(' '.join(doc)) for doc in docs_lemmatized]
    
    bag = []
    for doc in docs_no_mentions:
        if len(doc) >= 2:
            bag.append(doc)
    
    # converts into list of lists
    bow = [list(tweet.split(' ')) for tweet in bag]
    
    
    # convert docs into pd series
    full_service_docs_series = pd.Series( (v[0] for v in bow) )
    
    # changed docs stemmed to docs lemmatized
    return bag, bow, docs_lemmatized, full_service_docs_series
