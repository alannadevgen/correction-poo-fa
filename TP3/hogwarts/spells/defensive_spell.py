from spells.spell import Spell
from characters.character import Character


class DefensiveSpell(Spell):
    def __init__(self, name: str, healing: int):
        super().__init__(name, 0)
        self.healing = healing

    def cast(self, caster: Character, target: Character = None) -> bool:
        if self.can_cast():
            caster.heal(self.healing)
            self.cooldown = self.max_cooldown
            return True
        return False
