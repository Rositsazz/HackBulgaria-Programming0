n = input("Enter number: ")
n = int(n)

new_integer = 0
old_integer = n

while n>0 :
    digit = n%10
    new_integer = new_integer*10 + digit
    n = n//10

if new_integer==old_integer:
    print("Palindrom")
else:
    print("Not Palindrom")
