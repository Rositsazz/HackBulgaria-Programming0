number = input("enter number")
number = int(number)
print(number)

a = number%10
print(a)

number = number//10
b = number%10
print(b)

number = number//10
c = number%10
print(c)

best = 0
bigger = 0
maxn = 0
minn = 0

if a>b and a>c:
    best = a
    if b>c:
        bigger = b
        maxn = a*100+b*10+c
        print(maxn)
        minn = c*100+b*10+a
        print(minn)
        
    elif c>b:
        bigger = c
        maxn = a*100+c*10+b
        print(maxn)
        minn = b*100+c*10+a
        print(minn)  
        
elif b>a and b>c :
    best = b
    if a>c:
        bigger = a
        maxn = b*100+a*10+c
        print(maxn)
        minn = c*100+a*10+b
        print(minn)
        
    elif c>a:
        bigger = c
        maxn = b*100+c*10+a
        print(maxn)
        minn = a*100+c*10+b
        print(minn)
        
elif c>a and c>b :
    best = c
    if a>b:
        bigger = a
        maxn = c*100+a*10+b
        print(maxn)
        minn = b*100+a*10+c
        print(minn)
        
    elif b>a:
        bigger = b
        maxn = c*100+b*10+a
        print(maxn)
        minn = a*100+b*10+c
        print(minn)
