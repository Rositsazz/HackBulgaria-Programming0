points = input('Test points: ')
points = int(points)

min_points = 0
max_points = 100

if min_points <= points and points <= max_points :
    
    if points <= 50 :
        print('Слаб 2')
        
    elif 51 <= points and points <= 60 :
        print('Среден 3')
        
    elif 61 <= points and points <= 70 :
        print('Добър 4')

    elif 71 <= points and points <= 80 :
        print('Много Добър 5')

    elif 81 <= points and points < 100 :
        print('Отличен 6')

    elif points == max_points :
        print('Много Отличен 7')

else :
    print('Incorrect test points!')
