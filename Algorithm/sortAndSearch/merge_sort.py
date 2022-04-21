from cProfile import run
from heapq import merge


def merge_sort(input_arr):
    len_arr = len(input_arr)
    if len_arr < 2:
        return input_arr
    middle_arr = len_arr // 2
    left = input_arr[:middle_arr]
    right = input_arr[middle_arr:]
    print("left:", left)
    print("right:", right)
    left = merge_sort(left)
    right = merge_sort(right)

    input_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            input_arr.append(left.pop(0))
        else:
            input_arr.append(right.pop(0))

    for elm in left:
        input_arr.append(elm)

    for elm in right:
        input_arr.append(elm)
    print("result:", input_arr)
    return input_arr

my_arr = [2, 8, -2, 3, 0, 6]
print("before:", my_arr)
print(merge_sort(my_arr))