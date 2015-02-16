number = input("Enter first number: ")
number = int(number)
number1 = input("Enter second number: ")
number1 = int(number1)

final_number = 0
if number > number1:
    start = number1
    end = number
elif number < number1:
    start = number
    end = number1

i = start
s = 0


while i<=end :
    s = i
    digit = 0
    if (s//10) == 0 :
        print("Sum of digits of " + str(i) + " = " + str(i))
    else : 
        while (s//10) != 0 :
            r = s%10
            digit+=r
            s=s//10
        print("Sum of digits of " + str(i) + " = " + str(digit+1))
    i+=1







