# Final Project Code for UN General Debates

# tf-idf is used to find which words have received the most attention in these debates and how these words have changed over the years and for different countries
# this could help us to find a pattern between the words
# specific attention is given to words related to climate change

import re
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
# install to dict in terminal

with open('/Users/sayali/Desktop/Columbia/QMSS/Courses/4 NLP Journalism/Final Project/un-general-debates.csv') as file:
    corp = file.read()

# open file

regex = re.findall('([0-9,]*[0-9][A-Z,"]*)*', corp)

# tells us the years of the sessions, the session number and the countries that spoke at the sessions

# create dictionary of data file

df = pd.read_csv("/Users/sayali/Desktop/Columbia/QMSS/Courses/4 NLP Journalism/Final Project/un-general-debates.csv")

undebates_dict = df.set_index('country').T.to_dict('list')

text = undebates_dict

# check key-value pairs in dictionary

text.keys()

# keys are countries; values are speeches

# clean dictionary values

# put in a list

speech = text.values()
speech = list(text.values())

len(speech) # to find number of lists

speech_str = str(speech) # turn lists back to strings
speech_tokenize = word_tokenize(speech_str)
speech_tokenize_str = str(speech_tokenize)

# iterate over the length of speech

# clean the file and remove stop words

stop_words = stopwords.words('english') + list(punctuation)

clean_speech = [] # create empty list

for x in speech_str:
    x = [w.lower() for w in x]
    x = [w for w in x if w not in stop_words]
    clean_speech.append(x)

# get list of keys and values here are the countries
countries = text.keys()
countries = list(text.keys())

# print for a variable eg IND (a key)

# there might be duplicated keys
# combine with + sign
# generate new list without duplicates

countries_str = str(countries)
countries_tokenize = word_tokenize(countries_str)

# match the keys with the values
countries_tokenize = [y for y in speech_tokenize]
countries_final = countries_tokenize


# commence tf-idf

# the corpus is the speeches given by different countries in all the years; the goal is to find differences and trends between them

# choose n-gram range and apply tf-idf

vectorizer = TfidfVectorizer(ngram_range = (1,2))
vectors = vectorizer.fit_transform(countries_final) # list of ngrams in corpus with countries as variables
feature_names = vectorizer.vocabulary_ # when feature_names cant be used due to the attribute error
dense = vectors.todense()
denselist = dense.tolist()

# create a data frame
df = pd.DataFrame(denselist, columns=feature_names, index=countries_final)

df_t = df.T # transpose the data frame

# analyze data frame and pick top n results

df_t.nlargest(100, IND)
df_t.nlargest(100, USA)
df_t.nlargest(100, BRA)
df_t.nlargest(100, CHI)
df_t.nlargest(100, FRA)
df_t.nlargest(100, MEX)
df_t.nlargest(100, NOR)

# explore specific terms with df[term]
df[climate]
df[climate change]
df[environment]
df[climate policy]
df[green]

# use appropriate regex again to find the most frequent terms and the words surrounding them






