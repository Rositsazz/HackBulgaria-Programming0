a = input("Enter the first number:")
a = int(a)
b = input("Enter the second number:")
b = int(b)

last_a = a%10
last_b = b%10

if last_a > last_b :
    print(a)

if last_b > last_a :
    print(b)

if last_b == b%10 :

    if a>=b :
        print(a)
    else:
        print(b)
