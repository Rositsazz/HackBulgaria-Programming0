def count_vowels_consonants(word):

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    i = 0
    j = 0

    for element in word:

        #print(element)
        if element in vowels:
            i+=1
        elif element in consonants:
            j+=1

    result = {
                "vowels":i,
                "consonants":j,
               }

    return result

print(count_vowels_consonants("aertyuioplhmndhsdgdirkf"))

