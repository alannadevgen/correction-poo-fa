from abc import ABC, abstractmethod

class AbstractMagicalItem(ABC):
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.owner = None

    def assign_to(self, wizard):
        self.owner = wizard
        wizard.magical_items.append(self)

    @abstractmethod
    def activate(self) -> bool:
        pass