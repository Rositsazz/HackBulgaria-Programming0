a = input("Enter lower bound:")
b = input("Enter upper bound:")
a = int(a)
b = int(b)

if a <= b :
    counter = a
    while counter <= b :
        if counter%2==0 :
            print(counter , "- even")
        else :
            print(counter , "- odd")
        counter = counter + 1
elif a >= b : 
    counter = b
    while counter <= a :
        if counter%2==0 :
            print(counter , "- even")
        else :
            print(counter , "- odd")
        counter = counter + 1
