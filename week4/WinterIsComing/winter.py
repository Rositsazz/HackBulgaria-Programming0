
seasons = ["winter","srping","summer", "srping","srping","summer", "srping","summer","spring"]

def winter_is_coming(seasons):
    counter = 0

    for index in range(0,len(seasons)):

        season = seasons[index]
        if season == "winter" :
            counter = 0
        else :
            counter+=1
    if counter >= 5:
        return True

    return False

funct = winter_is_coming(seasons)
print(funct)
