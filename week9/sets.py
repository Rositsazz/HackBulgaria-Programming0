def setify(a):
    new_list = []
    for number in a:
        if number not in new_list:
            new_list.append(number)

    return new_list
# vzima spisyk i go pravi v mnojestvo -
# koeto znachi che nqma povtarqshti se elementi


def diff(a, b):
    items1 = setify(a)
    items2 = setify(b)
    new_list = []
    for item in items1:
        if item not in items2:
            new_list.append(item)

    return new_list


def union(a, b):
    new_list = []
    for item in a:
        new_list.append(item)
    for item in b:
        new_list.append(item)
    return setify(new_list)


def union2(a, b):
    return setify(a+b)


def intersection(a, b):
    items1 = setify(a)
    items2 = setify(b)
    new_list = []
    for item in items1:
        if item in items2:
            new_list.append(item)

    return new_list


def cartesian_product(a, b):
    items1 = setify(a)
    items2 = setify(b)
    new_list = []
    for item in items1:
        for i in items2:
            new_list.append((item, i))

    return new_list


def main():
    print(setify([10, 0, 1, 1, 5, 5, 6]))
    print(setify([10, 0, 1, 1, 5, 5, 6, 0, 1]) == [10, 0, 1, 5, 6])
    print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
    print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
    print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
    print(cartesian_product([0, 1, 2], [0, 1]))
    print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


if __name__ == '__main__':
    main()
