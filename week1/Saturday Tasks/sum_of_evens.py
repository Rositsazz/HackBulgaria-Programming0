number = input("Enter a number:")
number= int(number)

if number%2==0 :
    print("even")
    suma=0
    i=0
    while i<=number:
        suma = suma + i
        i+=2
else :
    print("odd")
    suma = 0
    i=0
    while i<number :
        suma = suma + i
        i+=2  

print(suma)
