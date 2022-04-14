from abc import ABCMeta, abstractmethod


class AbstactFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_chair(self) -> "AbstractChair":
        pass
    
    @abstractmethod
    def create_sofa(self) -> "AbstractSofa":
        pass
    
    @abstractmethod
    def create_table(self) -> "AbstractCoffeTable":
        pass


class ConcreteFactoryModern(AbstactFactory):
    def create_chair(self):
        return ModernChair()
    
    def create_sofa(self):
        return ModernSofa()

    def create_table(self):
        return ModernCoffeTable()


class ConcreteFactoryVictorian(AbstactFactory):
    def create_chair(self):
        return VictorianChair()
    
    def create_sofa(self):
        return VictorianSofa()

    def create_table(self):
        return VictorianCoffeTable()

class ConcreteFactoryArt(AbstactFactory):
    def create_chair(self):
        return ArtChair()
    
    def create_sofa(self):
        return ArtSofa()

    def create_table(self):
        return ArtCoffeTable()

class AbstractChair(metaclass=ABCMeta):

    @abstractmethod
    def sit_on(self):
        pass

class AbstractSofa(metaclass=ABCMeta):

    @abstractmethod
    def lamidan(self):
        pass

class AbstractCoffeTable(metaclass=ABCMeta):

    @abstractmethod
    def drinking(self):
        pass

class ModernChair(AbstractChair):

    def sit_on(self):
        print("modern sandali")


class ModernSofa(AbstractSofa):

    def lamidan(self):
        print("modern sofa")


class ModernCoffeTable(AbstractCoffeTable):

    def drinking(self):
        print("modern miz")


class ArtChair(AbstractChair):

    def sit_on(self):
        print("Art sandali")


class ArtSofa(AbstractSofa):

    def lamidan(self):
        print("Art sofa")


class ArtCoffeTable(AbstractCoffeTable):

    def drinking(self):
        print("Art miz")

class VictorianChair(AbstractChair):

    def sit_on(self):
        print("Victorian sandali")


class VictorianSofa(AbstractSofa):

    def lamidan(self):
        print("Victorian sofa")


class VictorianCoffeTable(AbstractCoffeTable):

    def drinking(self):
        print("Victorian miz")

def client(factory: AbstactFactory):

    chair = factory.create_chair()
    chair.sit_on()

    sofa = factory.create_sofa()
    sofa.lamidan()

    table = factory.create_table()
    table.drinking()


if __name__ == "__main__":
    print("mahsulat modern")
    khate_tolid_modern = ConcreteFactoryModern()
    client(khate_tolid_modern)

    print("mahsulat victorian")
    khate_tolid_victorian = ConcreteFactoryVictorian()
    client(khate_tolid_victorian)

    print("mahsulat art")
    khate_tolid_art = ConcreteFactoryArt()
    client(khate_tolid_art)