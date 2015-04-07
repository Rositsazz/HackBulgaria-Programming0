def swap(i, j, lst):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

# a = [1, 2]
# swap(0, 1, a)
# print(a)


def first_selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for k in range(i + 1, len(numbers)):
            if numbers[k] < numbers[min_index]:
                min_index = k
        swap(min_index, i, numbers)


# a = [11, 3, 55, 6, 4]
# selection_sort(a)
# print(a)


def min_element(start_index, numbers):
    min_index = start_index
    index = start_index
    while index < len(numbers):
        if numbers[index] < numbers[min_index]:
            min_index = index
        index += 1

    return min_index


def selection_sort2(numbers):
    for i in range(len(numbers)):
        min_el = min_element(i, numbers)
        swap(i, min_el, numbers)


def selection_sort3(numbers):
    new_list = numbers[:]
    print(new_list)
    for i in range(len(new_list)):
        min_el = min_element(i, new_list)
        swap(i, min_el, new_list)

    return new_list


def diff(items1, items2):
    result = []
    for a in items1:
        if a not in items2:
            result.append(a)

    return result


def min_element2(start_index, numbers):
    min_index = start_index
    index = start_index
    while index < len(numbers):
        if numbers[index] < numbers[min_index]:
            min_index = index
        index += 1

    return min_index


s = [11, 3, 2, 2, 6, 4, 7]
# print(min_element2(0, s))


def mini(numbers):
    min_index = 0
    index = 0
    while index < len(numbers):
        if numbers[index] < numbers[min_index]:
            min_index = index
        index += 1

    return numbers[min_index]


def func_with_unique_elements(numbers):
    min_el = mini(numbers)
    new_list = []
    for i in range(len(numbers)):
        min_el = mini(diff(numbers, new_list))
        new_list.append(min_el)
    return new_list


# print(func_with_unique_elements(s))


def min_index_without_used(numbers, used):
    unused_indexes = diff(range(len(numbers)), used)

    min_index = unused_indexes[0]
    for index in unused_indexes:
        if numbers[index] < numbers[min_index]:
            min_index = index

    return min_index


def selection_sort(numbers):
    res = []
    n = len(numbers)
    used = []

    while len(res) != n:
        min_index = min_index_without_used(numbers, used)
        used.append(min_index)
        res.append(numbers[min_index])

    return res

print(selection_sort(s))
