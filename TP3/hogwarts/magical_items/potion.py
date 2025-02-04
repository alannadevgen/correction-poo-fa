from magical_items.abstract_magical_item import AbstractMagicalItem

class Potion(AbstractMagicalItem):
    def __init__(self, name: str, effect: str, power: int):
        super().__init__(name, power)
        self.effect = effect
        self.used = False

    def activate(self) -> bool:
        if not self.used:
            self.used = True
            return True
        return False