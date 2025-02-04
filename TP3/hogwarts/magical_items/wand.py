from magical_items.abstract_magical_item import AbstractMagicalItem

class Wand(AbstractMagicalItem):
    def __init__(self, name: str, wood: str, core: str):
        super().__init__(name, 8)
        self.wood = wood
        self.core = core
        self.spell_capacity = 10
        self.current_charge = 10

    def activate(self) -> bool:
        if self.current_charge > 0:
            self.current_charge -= 1
            return True
        return False

    def recharge(self, power: int = 5):
        self.current_charge = min(10, self.current_charge + power)