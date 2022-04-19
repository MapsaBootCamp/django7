from abc import ABCMeta, abstractmethod

class Target(metaclass=ABCMeta):

    @abstractmethod
    def data_transform(self):
        pass

class StockService:

    def get_data(self):
        print("ravand gereftan data az service stock. gharare xml bede")
        return "stock xml data"

class AdapterSakhtJson(Target, StockService):

    def data_transform(self):
        data = self.get_data()
        print("ravand tabdil be json")
        return  "stock json data"


# class AdapterSakhtJson(Target):
    
#     def __init__(self) -> None:
#         self.__adaptee: StockService = StockService()

#     def data_transform(self):
#         data = self.__adaptee.get_data()
#         print("ravand tabdil be json")
#         return  "stock json data"

# class AdapterSakhtCSV(Target):
#     def __init__(self) -> None:
#         self.__adaptee: StockService = StockService()

#     def data_transform(self):
#         data = self.__adaptee.get_data()
#         print("ravand tabdil be csv")
#         return  "stock csv data"

