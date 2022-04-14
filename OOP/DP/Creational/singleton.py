from typing import Any

# class Singlton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#             if not Singlton._instance:
#                 Singlton._instance = super().__new__(cls, *args, **kwargs)
#             return Singlton._instance



class MetaSinglton(type):
    _instances = {} 

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in MetaSinglton._instances:
            MetaSinglton._instances[self] = super().__call__(*args, **kwds)
        return MetaSinglton._instances[self]


class A(metaclass=MetaSinglton):
    pass

class B(metaclass=MetaSinglton):
    pass


a1 = A()
a2 = A()

b1 = B()
b2 = B()

print("a1", id(a1))
print("a2", id(a2))
print("b1", id(b1))
print("b2", id(b2))