# data types: int, float, str, bool, complex
import os

a = True
print("bar aval: ", type(a))
a = 35
print("bar dovom: ", type(a))

# operations: +,-, , *, /, %, //, **, +=
# a /= 2 #   a = a /2
# operations: not, and, or
# operations: <, >, >=, <=, ==, !=
# operations: is, not is

if a > 18:
    print("mojaz")
elif 15 < a < 18:
    print("kam mojaz")
else:
    print("na mojaz")


# loop in python: while, for

# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 3 == 0:
#         continue
#     print("*" * counter)

# data structure: list [], tuple (), set {}, dictionary {key: value}

my_list = [2, 2.5, "Ashkan", [2, 4], True] # iterable, mutable, indexable, ...
# range(10) ----> 0, 1, ..., 9
# range(10, 20) ----> 10, 11, ..., 19
# range(10, 20, 2) ----> 10, 12, ..., 18

# counter = 1

# for naneh_ghamar in my_list:
#     print(f"elm dafe {counter}: ", naneh_ghamar)
#     counter += 1


# for i in range(12): #   for(int i = start; i < end ; i++)
#     print("i: ", i)
# length = int(input("length: "))   # casting int(), float(), str(), list(), tuple(), bool(), ...
# height = int(input("heigth: "))

# # print("* " * length)
# # for i in range(1, height - 1):
# #     print("* " + "  " * (length - 2) + "*")
# # print("* " * length)
# os.system('clear')

# for i in range(height):
#     if (i == 0) or (i == height - 1):
#         print("* " * length)
#     else:
#         print("* " + "  " * (length - 2) + "*")

        
##### 2, 3, 5, 7, 11, 13

def is_prime(num : int) -> bool:
    if num < 0:
        raise Exception("adad bayad mosbat bashashad")

    if num == 1:
        return False
    for i in range(2, num ** 0.5):
        if num % i == 0:
            return False
    
    return True



if is_prime(int(input("adadat ra begu: "))):
    print("aval ast")
else:
    print("aval nist")