from abc import ABC

class Spell(ABC):
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
        self.cooldown = 0
        self.max_cooldown = 2

    def can_cast(self) -> bool:
        return self.cooldown == 0

    def cast(self, caster, target) -> bool:
        if self.can_cast():
            target.take_damage(self.damage)
            self.cooldown = self.max_cooldown
            return True
        return False

    def update_cooldown(self):
        self.cooldown = max(0, self.cooldown - 1)
