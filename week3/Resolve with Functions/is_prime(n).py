
def is_prime(n):
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
    return is_prime


numbers  = [0, 2, -2, 5, 10]
func = is_prime(13)


print (func)
