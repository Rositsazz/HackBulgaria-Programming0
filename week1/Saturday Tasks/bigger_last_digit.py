a = input("Enter the first number:")
a = int(a)
b = input("Enter the second number:")
b = int(b)

if a%10 > b%10 :
    print(a)
if b%10 > a%10 :
    print(b)
if a%10 == b%10 :
    if a>=b :
        print(a)
    else:
        print(b)
