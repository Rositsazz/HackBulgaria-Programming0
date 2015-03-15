number = input("Enter number:")
number = int(number)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)

def fib_number(n):
    result = ""
    i = 1
    while i <= n:

        result+=str(F(i))

        i+=1

    return result

print(fib_number(number))
