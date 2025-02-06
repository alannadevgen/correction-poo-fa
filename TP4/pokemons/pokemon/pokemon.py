from pokemon.exceptions import IncorrectPokemonException


class Pokemon:
    def __init__(self, name: str, type: str, hp: int, attack: int):
        if hp < 0 or attack < 0:
            raise IncorrectPokemonException("HP and attack must be positive")
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack

    def __str__(self) -> str:
        return f"{self.name} ({self.type}) - HP: {self.hp}, ATK: {self.attack}"

    def fight(self, other: "Pokemon") -> None:
        if self.hp <= 0:
            raise IncorrectPokemonException(f"{self.name} is KO and cannot attack!")
        other.hp = max(0, other.hp - self.attack)
