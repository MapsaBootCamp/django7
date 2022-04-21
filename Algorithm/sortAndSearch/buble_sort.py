def buble_sort(input_arr):

    for i in range(len(input_arr) - 1):
        for j in range(len(input_arr) - i - 1):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j] # swap


    return input_arr


my_arr = [2, 8, -2, 3, 0, 6]
print(buble_sort(my_arr))