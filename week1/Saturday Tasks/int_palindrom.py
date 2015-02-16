number = input("Enter number: ")
number = int(number)
string = ""
v = number
counter = 0
while number != 0:

    string+=str(number%10)
    number = number//10
    counter = counter +1
print(string)


if v == int(string):
    print("Palindrom")
else :
    print("Not")
