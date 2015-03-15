def count_zero_neighbours2(numbers):

    length = len(numbers)
    counter = 0
    for i in range(0,length):
        for j in range(i,length) :
            x = numbers[i]
            y = numbers[j]
            if x + y == 0 :
                counter+=1

    return counter

def count_zero_neighbours1(numbers):

    length = len(numbers)
    counter = 0
    for i in range(0,length):
        for j in range(i+1,length) :
            x = numbers[i]
            y = numbers[j]
            if x + y == 0 :
                counter+=1

    return counter

def is_prime(n):
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
    return is_prime

def prime_pair(numbers):

    prime = False
    for item in numbers :
        if is_prime(count_zero_neighbours1(numbers)) :
            prime = True
            return prime

    return prime



numbers  = [0, 2, -2, 5, 10]
func = count_zero_neighbours2(numbers)
prime = prime_pair(numbers)
#print(prime)
print (func)
