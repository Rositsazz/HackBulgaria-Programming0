def head(lst) :
    first = lst[0]
    return first


def last(lst) :
    last_element = lst[len(lst)-1]
    return last_element

def tail(lst) :
    lst.pop(0)
    return lst
#take(2,[1,2,3,4]) -> [1,2]
#behead([1,2,3,4]) -> [2,3,4]
#tail([1,2,3,4]) -> [2,3,4]
#drop(2,[1,2,3,4]) -> [3,4]

def equal_lists(list1,list2) :
    if len(list1)==len(list2):
        if list1==list2 :
            return True
    return False

def count_item(item,lst) :
    counter = 0
    for element in lst :
        if element==item:
            counter+=1
    return counter

def take(number,lst) :
    new_list = lst[0:number]
    return new_list

def drop(number,lst):
    new_list = lst[number:len(lst)]
    return new_list

def drop1(number,lst):
    new_list = lst[number:len(lst)]
    return new_list

def reverse(lst) :
    lst.reverse()
    return lst

def behead(lst):
def tail(lst) :
    return drop(1,items)

def sublist(list1,list2):
    n = len(list1)
    while len(list2)!=0 :
        if take(n,list2) == list1 :
            return True
        list2 = behead(list2)

    return False
