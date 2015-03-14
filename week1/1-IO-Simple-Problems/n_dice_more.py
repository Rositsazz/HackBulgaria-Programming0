from random import randint

number = input ('Enter sides:')
number = int(number)

i = 1
suma = 0
while i <= 3:
    roll = randint(1,number)
    print(str(i) + " roll:" + str(roll))
    suma += roll
    i+=1

print('The sum is:',suma)
