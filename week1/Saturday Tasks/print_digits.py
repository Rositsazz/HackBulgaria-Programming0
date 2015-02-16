number = input("Enter a number:")
number= int(number)


while number%10 != number//10 :
    print(number%10)
    number = number//10


