import abc
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def geeks(self):
        return 'Parent class'

class Child(Parent):
    @property
    def geeks(self):
        return 'Child class'

try:
    parent  =   Parent()
    print(parent.geeks())
except Exception as err:
    print(err)

child   =   Child()
print(child.geeks)