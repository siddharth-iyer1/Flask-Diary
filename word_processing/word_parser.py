import string
import word_cleaner

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


entry = "No quiz in recitation yk what that means. Met up w Boris to do project, I think we're becoming a lot better friends. We joke around a lot more ab random shit and its pretty cool! He's an inspirational dude and I might hang w him Sunday morning if its possible for both of us. Gonna try and knock a good amount of work out Sat morning so its not stressful or anything. Also project is moving, hope its not too hard man Saw Arushi after! Got lunch and pulled up to her place. I feel bad for how I often feel that she's an annoying person, but tbh I really don't know how to get over that stuff. I honestly wish she was a better listener and didn't just blurt random shit sometimes. She can say hurtful things, and the thing that I don't like is that when she's wrong she'll double down? Even though today was fun with her and friends, I just be thinking about that stuff anyways. Is that wrong? Not too sure but glad I'm not internalizing it too much. Then saw Janvi, Aneri, Samik. Really glad Samik is out of his shell. Bro is enjoying himself around everyone and says fun dumb shit all the time. It's really nice to see this shift. Closer to the end of sophomore year means things are settling, which is great. Came back did work. TC mixer was mid asf but left with Jiya and she agreed and I thought that was awesome. Cool person, idk if we'll be great friends but that was nice. Bumped into Adi and that was so positive. Really enjoyed that. Texting Medha too rn and learning a lot about her. idk why I feel weird writing here about this. These are my thoughts bruh. It's nice seeing her open up. Really wanna hang w her this week and just make some headway yk. Just be fully straight about stuff. Overall solid day. Lots of work done. Gonna keep going, let's get this shi. Thankful For: Understanding that I enjoy my alone time Things to Work On: Solidifying my circles, Not internalizing thoughts about people To do list: Be a consistent guy for everyone Be a good man See Amma tomorrow at temple, mannnn its so late"
words = word_cleaner.remove_punctuation(entry)
data = word_cleaner.remove_stop_words(words)


dict = {}
populate_dict(dict, data)
result = arrange(dict)

print(result)