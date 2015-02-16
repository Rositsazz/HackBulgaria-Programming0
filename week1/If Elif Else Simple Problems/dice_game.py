from random import randint
number = input('Dices: ')
name1 = input('First player: ')
name2 = input('Second player: ')
dice1 = randint(1,int(number))
dice2 = randint(1,int(number))
print(name1 + ' rolls ',dice1)
print(name2 + ' rolls ',dice2)
if dice1<dice2:
    print(name2 + ' wins')
elif dice1>dice2:
    print(name1 + ' wins')
