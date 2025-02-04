from abc import ABC
from typing import List, Optional
from spells.spell import Spell

class Character(ABC):
    def __init__(self, name: str, max_health: int):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.spells: List[Spell] = []

    def learn_spell(self, spell: Spell):
        self.spells.append(spell)

    def take_damage(self, amount: int):
        self.current_health = max(0, self.current_health - amount)

    def heal(self, amount: int):
        self.current_health = min(self.max_health, self.current_health + amount)

    def select_spell(self, spell_name: str) -> Optional[Spell]:
        for spell in self.spells:
            if spell.name == spell_name and spell.can_cast():
                return spell
        return None

    def is_alive(self) -> bool:
        return self.current_health > 0

    def update_spells(self):
        for spell in self.spells:
            spell.update_cooldown()