number = input("Please, enter a number n: ")
number = int(number)
list_of_digits = []
while number!=0 :
    digit = number%10
    list_of_digits += [digit]
    number = number//10
list_of_digits.reverse()
print ("List of digits is: " ,list_of_digits)

i = 0
n = 0 
while i< len(list_of_digits) :
    n = n * 10 + list_of_digits[i]
    i+=1
print(n)
