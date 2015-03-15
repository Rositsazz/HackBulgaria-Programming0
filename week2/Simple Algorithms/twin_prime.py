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
    num2 = number + 2
    num1 = number - 2
    if is_prime_number(num2)==True and is_prime_number(num1)==True :

        print("Twin primes with " + str(number) + ":")
        print(num1,number)
        print(number,num2)

    elif is_prime_number(num2)==False and is_prime_number(num1)==False :

        print(str(number) + " is prime but:")
        print(str(num1)+" and " + str(num2)+ " are not " )

    elif is_prime_number(num2)==False and is_prime_number(num1)==True :

        print(str(number) + " is prime but:")
        print(str(num1)+"is not and " + str(num2)+ " is " )

    elif is_prime_number(num2)==True and is_prime_number(num1)==False :

        print(str(number) + " is prime but:")
        print(str(num2)+"is not and " + str(num1)+ " is " )

else :

    print(str(number)+ " is not prime")
