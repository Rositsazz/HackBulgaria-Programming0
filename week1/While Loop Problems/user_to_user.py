a = input("Enter lower bound:")
b = input("Enter upper bound:")
a = int(a)
b = int(b)

if a <= b :
    counter = a
    while counter <= b :
        print(counter)
        counter = counter + 1
elif a >= b : 
    counter = b
    while counter <= a :
        print(counter)
        counter = counter + 1
