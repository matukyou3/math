from abc import ABC, abstractmethod

class Group(ABC):
    @abstractmethod
    def generators(self):
        """群の生成元を返す"""
        pass
    
    @abstractmethod
    def multiply(self, a, b):
        pass
    
    @abstractmethod
    def identity(self):
        pass
    
    @abstractmethod
    def inverse(self, a):
        pass
    
class FiniteGroup(Group):
    @property
    @abstractmethod
    def elements(self):
        """有限群の場合のみ列挙可能"""
        pass
    
