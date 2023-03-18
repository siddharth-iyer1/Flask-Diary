import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import string

def remove_punctuation(entry):
    no_punct = entry.translate(str.maketrans('', '', string.punctuation))
    return no_punct.split()

def remove_stop_words(words):
    # Remove stop words from the list of words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    return words


entry = ""
entry = remove_punctuation(entry)
remove_stop_words(entry)