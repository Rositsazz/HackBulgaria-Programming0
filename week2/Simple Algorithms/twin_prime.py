number = input("Enter number: ")
number = int(number)

def is_prime_number (n):
    start = 2
    is_prime = True

    if n == 1:
        is_prime = False

    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start = start + 1
    return is_prime


if is_prime_number(number)==True :
    
    if is_prime_number(number+2)==True and is_prime_number(number-2)==True :
        print("Twin primes with " + str(number) + ":")
        print(number-2,number)
        print(number,number+2)
    elif is_prime_number(number+2)==False and is_prime_number(number-2)==False :
        print(str(number) + " is prime but:")
        print(str(number-2)+" and " + str(number+2)+ " are not " )
    elif is_prime_number(number+2)==False and is_prime_number(number-2)==True :
        print(str(number) + " is prime but:")
        print(str(number-2)+"is not and " + str(number+2)+ " is " )
    elif is_prime_number(number+2)==True and is_prime_number(number-2)==False :
        print(str(number) + " is prime but:")
        print(str(number+2)+"is not and " + str(number-2)+ " is " )
        
else :
    print(str(number)+ " is not prime")
