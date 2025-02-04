from spells.spell import Spell


class OffensiveSpell(Spell):
    def __init__(self, name: str, damage: int, element: str):
        super().__init__(name, damage)
        self.element = element
