
import sys

a = (i for i in range(10)) ## generator


a_dict = {"name": "Ashkan"}
b_dict = {"age": 28, "name": "Reza"}

print({**a_dict, **b_dict})


class A:
    __slots__ = "foo", "bar"
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

class B:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

a = A("fool", "bar")
b = B("fool", "bar")

a_list = [A("fool", "bar") for i in range(1000000000)]
b_list = [B("fool", "bar") for i in range(1000000000)]

print("instance of class with __slots__", sys.getsizeof(a_list))
# print("instance of class with __dict__", sys.getsizeof(b_list))



my_list = [12, 2, 3, 53, 9]
my_tuple = (12, 2, 3, 53, 9)

# my_list = []
# my_tuple = tuple()

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

def multiplier(n):
    name = "Ashkan"
    def a(t):
        print(name)
        return n * t
    return a

a_10 = multiplier(10)
a_12 = multiplier(12)
print(a_10(12))
print(a_12(12))
