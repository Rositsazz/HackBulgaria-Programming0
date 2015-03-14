a = input("Enter lower bound:")
b = input("Enter upper bound:")
a = int(a)
b = int(b)

if a <= b :
    number = a
    while number <= b :
        if number%2==0 :
            print(number , "- even")
        else :
            print(number , "- odd")
        number += 1

elif a > b :
    number = b
    while number <= a :
        if number%2==0 :
            print(number , "- even")
        else :
            print(number , "- odd")
        number += 1
