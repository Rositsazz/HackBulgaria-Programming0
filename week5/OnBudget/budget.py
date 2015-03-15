def on_budget(books, budget) :

    books.sort()
    sum_of_books = 0

    for book in books :
        sum_of_books += book

    counter = 0

    for book in books :

        if budget - book < 0 :
            break

        budget -= book
        sum_of_books -= book
        counter += 1

    res = {

    "books on budget" : counter,
    "loan" : max(0, sum_of_books - budget)
    }

    return res

