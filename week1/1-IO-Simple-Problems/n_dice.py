from random import randint

number = input ('Enter sides:')
number = int(number)

print ('The dice rolled:')
rolled =randint(1,number)
print(rolled)
