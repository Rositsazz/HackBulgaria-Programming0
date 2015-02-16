number = input("Enter number: ")
number = int(number)
string = ""

while number != 0:

    string+=str(number%10)

    number = number//10
print(string)

