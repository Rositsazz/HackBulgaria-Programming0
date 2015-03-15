def forecast(days) :

    snowing = 0
    raining = 0
    suns = 0

    for day in days :
        if day=="snow" :
            snowing+=1
        elif day=="rain" :
            raining+=1
        elif day=="sunshine" :
            suns+=1

    if raining>snowing and raining>suns :
        return "rain"

    elif suns>raining and suns>snowing :
        return "sunshine"

    elif snowing>suns and snowing>raining:
        return "snow"

    elif suns==snowing and suns!=raining:
        return "rain"

    elif suns==raining and raining!=snowing:
        return "snow"

    elif raining==snowing and raining!=suns:
        return "suns"

    elif suns==snowing and snowing==raining and suns==raining:
        return days[len(days)-1]

