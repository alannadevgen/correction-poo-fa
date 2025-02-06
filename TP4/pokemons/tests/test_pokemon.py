# test_pokemon.py
import unittest
from pokemon.pokemon import Pokemon
from pokemon.exceptions import IncorrectPokemonException


class TestPokemon(unittest.TestCase):
    def test_invalid_pokemon_creation(self):
        """Test creating a Pokemon with negative stats"""
        with self.assertRaises(IncorrectPokemonException):
            Pokemon("Pikachu", "Electric", -10, 50)

        with self.assertRaises(IncorrectPokemonException):
            Pokemon("Charizard", "Fire", 100, -20)

    def test_fight(self):
        """Test fight mechanics"""
        pikachu = Pokemon("Pikachu", "Electric", 100, 30)
        bulbasaur = Pokemon("Bulbasaur", "Grass", 100, 25)

        pikachu.fight(bulbasaur)
        self.assertEqual(bulbasaur.hp, 70)  # 100 - 30

        # Test that a KO Pokemon cannot fight
        pikachu.hp = 0
        with self.assertRaises(IncorrectPokemonException):
            pikachu.fight(bulbasaur)

    def test_pokemon_ko(self):
        """Test that HP cannot become negative"""
        pikachu = Pokemon("Pikachu", "Electric", 20, 30)
        charizard = Pokemon("Charizard", "Fire", 100, 50)

        charizard.fight(pikachu)
        self.assertEqual(pikachu.hp, 0)  # HP should be 0, not negative


if __name__ == '__main__':
    unittest.main()