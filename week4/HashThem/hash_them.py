def hash_them(keys, values):

    person = {}
    i = 0

    for i,key in enumerate(keys):

            if i<len(values):
                person[key]=values[i]
                i+=1
            else:
                person[key]=None

    return person

print(hash_them(["Ivan", "Maria"], [ 2]))

