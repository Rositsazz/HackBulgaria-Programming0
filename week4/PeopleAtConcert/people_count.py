def get_people_count(activity) :

    persons_on_concert = []
    counter = 0
    for person in activity:
        if person not in persons_on_concert :
            persons_on_concert += [person]
            counter += 1
    return counter
