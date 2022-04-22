def recursive_binary_search(arr_, search_q, start, end):
    if end < start :
        return -1
    mid = (end + start) // 2
    if search_q == arr_[mid]:
        return mid
    elif search_q > arr_[mid]:
        return recursive_binary_search(arr_, search_q, mid + 1, end)
    else:
        return recursive_binary_search(arr_, search_q, start, mid - 1)


def loop_binary_search(arr_, search_q):
    start = 0
    end = len(arr_)
    while True:
        mid = (end + start) // 2
        if end < start:
            return -1
        if search_q == arr_[mid]:
            return mid
        elif search_q > arr_[mid]:
            start = mid + 1
        else:
            end = mid - 1


arr_ = [2, 5, 12, 18, 19, 28, 54, 68, 99]

print(recursive_binary_search(arr_, 19, 0, len(arr_))) #### amir doos nadare! 2/2/01
print(loop_binary_search(arr_, 19))