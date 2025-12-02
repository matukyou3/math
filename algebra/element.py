from abc import ABC, abstractmethod

class GroupElement(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
