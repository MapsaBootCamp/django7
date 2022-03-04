my_set = {2, 3, 3, 3, 3, 3}  # nonsubcriptable, order, gheir tekrari(unique), 
# print(my_set)

my_list = [3, 4, 5, 3, 2, 4, 5, 5, 3] # mutable
x = 3
my_tuple = (3, 4, True, my_list, x) # immutable, hashable
my_tuple1 = (3, 4, True, my_list, x) # immutable
print("ghabl: ", my_tuple)
my_list.pop()
x = 12
print("badesh: ", my_tuple)
copy_my_list = my_list  #deep copy
copy_my_list.insert(3, "a")
print(my_tuple.count(True))

a_t = (2, 3)
b_t = (2, 3)

a_l = [2, 3]
b_l = [2, 3]

name = "Ashkan"
name = "Ashkan Divband"
b = "Ashkan Divband"
c = "Ashkan Divband"
d = "Ashkan Divband"
e = "Ashkan Divband"
print(id(a_l))
print(id(b_l))
# print("my_list: ", my_list)

# print(list(set(my_list)))

name = "ashkan"
for ch in name:
    # print(ch)
    pass

a = 313121
b = 313121
c = 313121


# list unique save order!
def unique_list(input_list):
    tmp_list = []
    for i in input_list:
        if i not in tmp_list:
            tmp_list.append(i)

    return tmp_list


test_list = [3, 4, 56, 4, 3, 56, 5]
print(unique_list(test_list))



# motavaziolazla

def paralelogram(ghaedeh, height):
    print(" "*(height - 1) + "*" * ghaedeh)
    for i in range(1, height - 1):
        print(" " * (height - i - 1) + "*" + " " * (ghaedeh -2) + "*")
    print("*" * ghaedeh)

paralelogram(54, 18)


def bmm(a, b):

    maghsum_a = [a]
    maghsum_b = [b]

    for i in range(1, a):
        if a % i == 0:
            maghsum_a.append(i)

    for i in range(1, b):
        if b % i == 0:
            maghsum_b.append(i)
    intesection_set = list(set(maghsum_a) & set(maghsum_b))
    return max(intesection_set)

def bmm2(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
    

print(bmm2(360 ** 8, 240 ** 12))
def find_max_array(input_list):
    pass



#### git

### git push  ----> az local mibare roye remote
### git pull  ----> az remote update ha rp miare roye local
### git clone  ----> az remote avalin bar miare roye local
