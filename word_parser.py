'''
Day Rating
Weight
Dict for Words and Frequency
'''

import string

def remove_punctuation(entry):
    no_punct = entry.translate(str.maketrans('', '', string.punctuation))
    return no_punct.split()

def populate_dict(dict, entry):
    for w in entry:
        if w not in dict:
            dict[w] = 1
        else:
            dict[w] += 1
    return dict

def arrange(data):
    # Convert the dictionary to a list of tuples
    data_list = list(data.items())

    #Create Max Heap
    n = len(data_list)
    for i in range(n//2-1, -1, -1):
        heapify(data_list, n, i)

    # Extract the elements from the heap in descending order
    result = []
    for i in range(n-1, -1, -1):
        result.append(data_list[0])
        data_list[0], data_list[i] = data_list[i], data_list[0]
        heapify(data_list, i, 0)

    return result


def heapify(data, n, i):
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
        heapify(data, n, largest)


entry = ""

dict = {}
entry = remove_punctuation(entry)
populate_dict(dict, entry)
result = arrange(dict)

print(result)