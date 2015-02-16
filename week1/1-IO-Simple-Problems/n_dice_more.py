import random
from random import randint
number = input ('Enter sides:')
print ('First roll:')
a =random.random()*int(number)//1
print(a)
print ('Second roll:')
b =random.random()*int(number)//1
print(b)
sum = a + b
print('The sum is:\n',sum)
dice = randint(1,int(number))
print(dice)
