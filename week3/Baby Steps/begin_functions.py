#n = input("Enter number: ")
#n = int(n)
def square(number):
    return number**2

def factoriel(number):

    product = 1

    while number!=1 :
        product*=number
        number=number - 1

    return product

#res1 = square (n)
#res2 = factoriel(n)
#print("square(" +str(n)+ ")==" + str(res1))
#print("factoriel(" +str(n)+ ")==" + str(res2))

def length(array):

    counter = 0
    for number in array :
        counter+=1

    return counter





#a = [4,5,6,7,8,9,0,8]
#res3 = length(a)
#print(res3)

def member(item,array):

    is_item_in_array = False
    for item in array :
        is_item_in_array=True

    return is_item_in_array

a = member(1,[1,2,3,4])
print(a)

def grades_that_pass(students, grades, limit):

    length =len(students)
    i = 0
    counter = []

    while i< length :
        if grades[i]>=limit:
            counter+=[students[i]]
        i+=1

    return counter

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)
print(result)
