from collections import Counter

def count_words(words):
    counts = Counter(words)
    return counts

b = ["words", "are", "meaningful", "words", "words", "are"]
print(count_words(b))

def count_words2(words):

    result = {}

    for word in words:
        if word in result :
            result[word]+=1
        else:
            result[word]=1

    return result

b = ["words", "are", "meaningful", "words", "words", "are"]
print(count_words2(b))
