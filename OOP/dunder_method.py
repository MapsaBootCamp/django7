class A:
    def __init__(self, investment):
        self.investment = investment

    def __add__(self, a2: "A"):
        temp = self.investment + a2.investment
        return A(temp)

    def __str__(self) -> str:
        return str(self.investment)

a1 = A(2000)
a2 = A(5000)
print(a1 + a2)
