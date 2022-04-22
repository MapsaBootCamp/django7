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

    def append(self, data):
        pass

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

print(l)