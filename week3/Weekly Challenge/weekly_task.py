n = input("Enter number:")
n = int(n)

def min_of_digits(n):

    array = []

    while n > 0 :
        num = n%10
        array += [num]
        n = n//10

    min_number = sorted(array)

    if min_number[0]==0:
        return False

    string1 = ""
    j = 0
    while j< len(min_number) :
        string1+=str(min_number[j])
        j+=1

    a=print(string1)

    return a

def max_of_digits(n):

    array = []

    while n > 0 :

        num = n%10
        array += [num]
        n = n//10

    max_number = sorted(array, reverse=True)

    if max_number[len(max_number)-1]==0:
        return False
    string2 = ""
    j = 0

    while j< len(max_number) :

        string2+=str(max_number[j])
        j+=1

    b=print(string2)

    return b



min_of_digits(n)

max_of_digits(n)
