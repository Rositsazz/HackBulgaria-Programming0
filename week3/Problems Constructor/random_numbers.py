from random import randint
def generate_random_list(n, start, end):
    list_numbers = []
    i = 0
    while i < n :
        list_numbers +=[ randint(start,end)]
        i+=1
    return list_numbers

print(generate_random_list(5,1,4))
    
