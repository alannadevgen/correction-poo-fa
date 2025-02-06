from pokemon import Pokemon
from exceptions import IncorrectPokemonException

class PokemonTrainer:
    def __init__(self, team: list[Pokemon]):
        self.team = team

    def choose_pokemon(self, pokemon) -> Pokemon:
        # Filter Pokemon that can still fight
        active_pokemons = [p for p in self.team if p.hp > 0]
        if not active_pokemons:
            raise IncorrectPokemonException("No Pokemon available for battle!")

        if pokemon not in active_pokemons:
            raise IncorrectPokemonException("Invalid Pokemon selected!")

        return pokemon

    def fight(self, opponent: Pokemon) -> None:
        try:
            pokemon = self.choose_pokemon()
            print(f"\nBattle between {pokemon.name} and {opponent.name}!")

            while pokemon.hp > 0 and opponent.hp > 0:
                # Trainer's turn
                pokemon.fight(opponent)
                print(
                    f"{pokemon.name} attacks! {opponent.name} has {opponent.hp} HP left")

                if opponent.hp <= 0:
                    print(f"{opponent.name} is KO!")
                    break

                # Opponent's turn
                opponent.fight(pokemon)
                print(
                    f"{opponent.name} counterattacks! {pokemon.name} has {pokemon.hp} HP left")

                if pokemon.hp <= 0:
                    print(f"{pokemon.name} is KO!")
                    break

        except IncorrectPokemonException as e:
            print(f"Error: {e}")