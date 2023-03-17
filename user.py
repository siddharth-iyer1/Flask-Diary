import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import string

class User:
    def __init__(self, pos_data, neg_data):
        self.pos_data = pos_data        # Of type journal data
        self.neg_data = neg_data

    def get_freq_list(self, journal_type):
        if journal_type == "Positive":
            return self.pos_data.freq_list
        elif journal_type == "Negative":
            return self.neg_data.freq_list


class journal_data:                     # Create an object for positive and negative journals
    def __init__(self, journals):
        self.journals = journals
        self.mega_string = "".join(self.journals)
        self.clean_mega_string
        self.freq_dict = {}
        self.freq_list = []
        self.stop_words = set(stopwords.words('english'))

    def add_journal(self, entry):
        self.journals.append(entry)
        self.mega_string = "".join(self.journals)
        self.clean_mega_string()

    def clean_mega_string(self):
        no_punct = self.mega_string.translate(str.maketrans('', '', string.punctuation))
        words = [word for word in words if word.lower() not in self.stop_words]
        self.mega_string = words

    def populate_dict(self):
        for w in self.mega_string:
            if w not in self.freq_dict:
                self.freq_dict[w] = 1
            else:
                self.freq_dict[w] += 1

    def arrange(self):
        # Convert the dictionary to a list of tuples
        data_list = list(self.freq_dict.items())

        #Create Max Heap
        n = len(data_list)
        for i in range(n//2-1, -1, -1):
            self.helper_heapify(data_list, n, i)

        # Extract the elements from the heap in descending order
        result = []
        for i in range(n-1, -1, -1):
            result.append(data_list[0])
            data_list[0], data_list[i] = data_list[i], data_list[0]
            self.helper_heapify(data_list, i, 0)

        self.freq_list = result

    def helper_heapify(self, data, n, i):
        # Heapify a subtree rooted at index i
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < n and data[left][1] > data[largest][1]:
            largest = left

        if right < n and data[right][1] > data[largest][1]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.helper_heapify(data, n, largest)
