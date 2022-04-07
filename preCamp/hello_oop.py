### attribute ----> variable
### attribute ---> instance attribute, class attribute
### method ----> functions
### method types ---> class method, instance method, static method, abstract method
### instance method ---> first argument ---> khode object 
### decorator ---> @
### Encapsulation, Inheritance, Polymorphism, Abstraction

class User:
    count = 0
        
    def __init__(self, username, password, age=None) -> None:
        self.username = username
        self.password = password
        self.age = age
        User.add_user()
    
    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
        else:
            print("password ro eshteb dadi")

    def add_father_name(self, nam_baba):
        self.nam_baba = nam_baba

    @staticmethod
    def salam_static():
        print("salam")

    @classmethod
    def tedad_user(cls):
        print(cls.count)

    @classmethod
    def add_user(cls):
        cls.count += 1


a = 3
a = "ashkan"


from copy import copy

user1 = User("Ashkan", "1234")
user2 = User("Asghar", "1234")

user1.add_father_name("Ali")
user1.tedad_user()