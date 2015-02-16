from random import randint
from random import randint
player1 = input("Player1's name: ")
player2 = input("Player2's name: ")
start1 = 1001
start2 = 1001
suma = 0

while start1 !=0 and start2 != 0:                  
    if start1 > 0 and start2 > 0:
        start1 = start1 - (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        start2 = start2 - (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        if start1 == 20 and (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)==30 ):
            start1=-10
        elif start2 == 20 and (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)==30 ):
            start2=-10
        print(player1 + " :" + str(start1))
        print(player2 + " :" + str(start2))
    elif start1 < 0 and start2 < 0:
        start1 = start1 + (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        start2 = start2 + (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        print(player1 + " :" + str(start1))
        print(player2 + " :" + str(start2))
    elif start1 < 0 and start2 > 0:
        start1 = start1 + (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        start2 = start2 - (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        print(player1 + " :" + str(start1))
        print(player2 + " :" + str(start2))
    elif start1 > 0 and start2 < 0:
        start1 = start1 - (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        start2 = start2 + (randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6))
        print(player1 + " :" + str(start1))
        print(player2 + " :" + str(start2))
print("final")

if start1 == 0 :
    print(player1 + " is the winner")
else :
    print(player2 + " is the winner")
    

