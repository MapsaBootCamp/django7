from tkinter.tix import NoteBook
from unittest import result


class LinkedList:

    class Element:
        def __init__(self, data) -> None:
            self.data = data
            self.next : "LinkedList.Element" = None

    def __init__(self) -> None:
        self.root : "LinkedList.Element" = None

    def add_begin(self, data):
        elm = LinkedList.Element(data)
        if not self.root:
            self.root = elm
        else:
            elm.next = self.root
            self.root = elm

    def append(self, data): # [a-> b -> 3 -> ]
        elm = LinkedList.Element(data)
        if not self.root:
            self.root = elm
        else:
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = elm
    
    def pop(self):
        if not self.root:
            raise Exception("linkde list is empty!")
        elif not self.root.next:
            result = self.root.data
            self.root = None
            return result
        else:
            temp = self.root
            while temp.next.next:
                temp = temp.next
            result = temp.next.data
            temp.next = None
            return result

    def __len__(self):
        count = 0
        temp = self.root
        while temp:
            temp = temp.next
            count += 1
        return count

    def __getitem__(self, x):
        if x < 0:
            x = x + len(self)
        if not self.root:
            raise IndexError("index is out of range linked list!")
        else:
            count = 0
            temp = self.root
            while count != x:
                temp = temp.next
                if not temp:
                    raise IndexError("index is out of range linked list!")
                count += 1

            return temp.data

    def __iter__(self):
        if not self.root:
            return
        else:
            temp = self.root
            while temp:
                yield temp.data
                temp = temp.next

    def __str__(self) -> str:
        result = "["
        temp = self.root
        while temp:
            result += str(temp.data)
            if temp.next:
                result += " -> "
            temp = temp.next
        result += "]"
        return result

l = LinkedList()
l.add_begin("Ashkan")
l.add_begin("Mapsa")
l.add_begin(3)
a = l.pop()
l.append("Amir")
l.append("Kebrit Meshgin")
print(l)
print(l[2])
print(len(l))
# for elm in l:
#     print(elm)