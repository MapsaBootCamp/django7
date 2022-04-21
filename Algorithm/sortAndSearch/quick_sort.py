def quick_sort(arr_ : list):
    if len(arr_) < 2:
        return arr_
    
    left = []
    right = []
    pivot = arr_.pop()

    for elm in arr_:
        if elm < pivot:
            left.append(elm)
        else:
            right.append(elm)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


my_arr = [2, 8, -2, 3, 0, 6]
print("before:", my_arr)
print(quick_sort(my_arr))