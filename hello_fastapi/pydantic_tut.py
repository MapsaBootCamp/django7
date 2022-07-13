from typing import Tuple
from pydantic import BaseModel


# class B:
#     __slots__: Tuple[str, ...] = tuple()

#     def __init__(self, name):
#         self.name = name

# b = B("Ashkan")
# print(b.name)

class A(BaseModel):
    id: int
    name : str
    active: bool = True

# a = A(s="a",id=12, name="ashkan", active=1)
a = A(name="ashkan",id=12, active=1)
print(a)