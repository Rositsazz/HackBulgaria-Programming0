import math
def is_triangle(a,b,c):
    lst = [a,b,c]
    lst = sorted(lst)
    if (lst[0]+lst[1]) > lst[2] :
        return True
    else :
        return False

def area(a,b,c):
    p = (a+b+c)/2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c) )
    return s

print(area(7,8,9))

def is_pythagorean(a,b,c):
    if is_triangle(a,b,c)==True:
        lst = [a,b,c]
        lst = sorted(lst)
        s = (lst[0])**2 + (lst[1])**2 
        if s == (lst[2])**2 :
            return True
        else :
            return False
    else :
        return False

def max_area(triangles):
    i = 0
    new_list = []
    while i<len(triangles):
        a=triangles[i][0]
        b=triangles[i][1]
        c=triangles[i][2]
        u=area(a,b,c)
        new_list+=[u]
        i+=1
    new_list=sorted(new_list)
    return new_list[len(new_list)-1]

triangles = [ [3, 4, 5], [7, 8, 9] ]
print(max_area(triangles))
