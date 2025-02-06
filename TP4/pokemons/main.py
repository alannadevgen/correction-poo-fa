from pokemon import Pokemon
from pokemon import PokemonTrainer

# Create some Pokemon
pikachu = Pokemon("Pikachu", "Electric", 100, 30)
charizard = Pokemon("Charizard", "Fire", 120, 40)
bulbasaur = Pokemon("Bulbasaur", "Grass", 95, 25)

# Create a trainer with a team
trainer = PokemonTrainer([pikachu, charizard, bulbasaur])

# Battle against a wild Pokemon
wild_pokemon = Pokemon("Pidgey", "Normal", 80, 20)
trainer.fight(wild_pokemon)