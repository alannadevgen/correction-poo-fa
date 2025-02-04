from characters.character import Character
from typing import List
from magical_items.abstract_magical_item import AbstractMagicalItem

class Wizard(Character):
    def __init__(self, name: str, magic_type: str):
        super().__init__(name, 100)
        self.magic_type = magic_type
        self.magical_items: List[AbstractMagicalItem] = []

    def magical_attack(self, target: 'Wizard', spell_name: str) -> bool:
        spell = self.select_spell(spell_name)
        if spell:
            return spell.cast(self, target)
        return False

    def activate_magical_item(self, item_name: str):
        for item in self.magical_items:
            if item.name == item_name:
                return item.activate()
        return False