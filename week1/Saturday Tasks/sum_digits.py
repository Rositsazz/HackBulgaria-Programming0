number = input("Enter a number: ")
number = int(number)

sum = 0
while number != 0:
    sum+=number%10
    number = number//10
   # print(number)
print(sum)
