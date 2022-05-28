from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofSides(self):
        pass

class Triangle(Polygon):
    pass

segiTiga    =   Triangle()
segiTiga.noofSides()