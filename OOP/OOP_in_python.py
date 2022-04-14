from typing import Any

# class A:
#     pass

# class B(A):
#     pass


# print("A is instance type:", isinstance(A, type))
# print("A is subclass type:", issubclass(A, type))

# print("A is subclass object:", issubclass(A, object))
# print("type is subclass object:", issubclass(type, object))
# print("object is instance type:", isinstance(object, type))
# print("type is instance object:", isinstance(type, object))
# print("object is subclass type:", issubclass(object, type))

####### method override and extend ----> super

class B:
    def salam(self, name):
        print("salam", name)

class D:
    def salam(Self, name):
        print("hello", name)


class C(B, D):
    def salam(self, name):
        print("salam bar jahan")
        super().salam(name)


# c = C()
# c.salam("Ashkan")

################### metaclass
class AMetaClass(type):

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call meta class")
        return super().__call__(*args, **kwds)
    
    def __str__(self) -> str:
        return "salam"

class A(metaclass=AMetaClass):

    def __init__(self) -> None:
        print("init khode class")
    
    def __new__(cls, *args, **kwargs):
        print("new khode class")
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, name) -> Any:
        print(name)

# a = A()


###### life cycle instance creation in python.... call Meta, new khode class, init khode class



#### abstraction

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def voice(self):
        pass
    
    @abstractmethod
    def gaz_gereftan(self) -> bool:
        pass

class Dog(Animal):
    
    def voice(self):
        print("vagh vagh")

class Doberman(Dog):

    def gaz_gereftan(self) -> bool:
        return True

class SageAhmagh(Dog):

    def gaz_gereftan(self) -> bool:
        return False


class Ghanari(Animal):

    def voice(self):
        print("chah chah")

    def gaz_gereftan(self) -> bool:
        return False


def sedaye_heivan(animal: Animal):
    animal.voice()

dog = Doberman()
sedaye_heivan(dog)

ghanari = Ghanari()
sedaye_heivan(ghanari)