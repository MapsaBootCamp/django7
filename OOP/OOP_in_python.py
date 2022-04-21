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

# dog = Doberman()
# sedaye_heivan(dog)

# ghanari = Ghanari()
# sedaye_heivan(ghanari)

##### dunder methods

def sal():
    print("sal")

class DunderTrain:
    _count = 12

    class Meta:
        pass

    def __init__(self) -> None:
        # print("salam!!")
        self.name = "Ashkan"
        self.__age = 12
        self._meta = sal

    def tarif_yek_attr_delkhah_shoma(self, attr_name, meghdar_avalieh):
        setattr(self, attr_name, meghdar_avalieh)
        print("salam")

    def __len__(self):
        return 12

    # def __del__(self):
    #     print("khodefz!!")

    def __delete__(self, instance):
        print(instance.camp)

    def __iter__(self, start=0, stop=15):
        while 1:
            yield start
            if start < stop-1:
                start +=1
            else:
                return

    # def __next__(self):
    #     if self.count > DunderTrain._count:
    #         raise StopIteration
    #     else:
    #         self.count += 1
    #         return self.count


    def __str__(self) -> str:
        pass


class BC:
    object_dundertrain = DunderTrain()


    def __init__(self) -> None:
        self.camp = "Django"


a = DunderTrain()
# b = DunderTrain()

# bc = BC()
# bc1 = BC()
# print(bc.exp.__dict__)
# del a
# print(bc.exp.__dict__)
# print("shart shirini")
# a._meta()
# print(len(a))


def range_khodemun(stop, start=0, step=1):
    while 1:
        yield start
        if start < stop -1:
            start +=1
        else:
            return


# for elm in range_khodemun(128):
#     print(elm)

a = DunderTrain()
# print(list(a))
# for elm in a:
#     print(elm)

a.tarif_yek_attr_delkhah_shoma("shahr", "tahran")
# print(a.__dict__)
# print(list(range_khodemun(12)))



class A:
    def __init__(self, name):
        self.name = name


class MixinSalamKardan:
    def salam(self):
        print("salam,", self.name)


class B(MixinSalamKardan, A):
    pass

a = B("Ashkan")
a.salam()



a = {}
a["name"] = "asghar"


a.update({"name": "Sakineh"})
# a.setdefault("name", "ashkan")
print(a)