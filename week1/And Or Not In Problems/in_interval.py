a=input('Enter the lower bound ''a'': ')
b=input('Enter the upper bound ''b'': ')
x=input('Enter number ''x'': ')
a=int(a)
b=int(b)
x=int(x)

if a < b:
    if x == a :
        print('The number is equal to the lower bound of the interval')

    elif x == b :
        print('The number is equal to the upper bound of the interval')

    elif a < x and x < b :
        print('The number is in the interval')

    elif x < a :
        print('The number is outside the interval, x < a')

    else :
        print('The number is outside the interval, x > b')

elif a>b or a==b :
    print('Invalid lower or upper bound')
