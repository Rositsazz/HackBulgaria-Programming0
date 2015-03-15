def calculate_coins(suma):

    moneti = [100,50,20,10,5,2,1]
    coins = {}
    suma = suma*100
    i = 0

    for coin in moneti:

        while True:
            if suma>=coin:
                suma = suma - coin
                i+=1
            else:
                coins[coin]=i
                i=0
                break

    return coins

s = calculate_coins(8.94)
print(s)

