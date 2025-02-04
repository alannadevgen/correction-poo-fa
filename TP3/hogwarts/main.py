from characters.wizard import Wizard
from magical_items.wand import Wand
from magical_items.potion import Potion
from spells.offensive_spell import OffensiveSpell
from spells.defensive_spell import DefensiveSpell
from hogwarts import Hogwarts

def main():
    # Création de Poudlard
    hogwarts = Hogwarts()

    # Création des personnages
    harry = Wizard("Harry Potter", "Gryffindor")
    draco = Wizard("Draco Malfoy", "Slytherin")

    # Création des objets magiques
    harry_wand = Wand("Phoenix Core Wand", "Holly", "Phoenix Feather")
    healing_potion = Potion("Healing Potion", "Restores health", 10)
    harry.magical_items.append(harry_wand)
    harry.magical_items.append(healing_potion)

    # Création des sorts
    expelliarmus = OffensiveSpell("Expelliarmus", 20, "Disarming")
    sectumsempra = OffensiveSpell("Sectumsempra", 30, "Bleeding")
    protego = DefensiveSpell("Protego", 15)
    harry.learn_spell(expelliarmus)
    harry.learn_spell(protego)
    draco.learn_spell(sectumsempra)

    # Inscription à Poudlard
    hogwarts.enroll_student(harry)
    hogwarts.enroll_student(draco)

    # Démonstration de combat
    print(f"Fight start - Harry: {harry.current_health}, Draco: {draco.current_health}")
    harry.magical_attack(draco, spell_name="Expelliarmus")
    print(f"Expelliarmus - Harry: {harry.current_health}, Draco: {draco.current_health}")
    draco.magical_attack(harry, spell_name="Sectumsempra")
    print(f"Sectumsempra - Harry: {harry.current_health}, Draco: {draco.current_health}")
    # Utilisation d'un objet magique
    harry.magical_attack(harry, spell_name="Healing Potion")
    print(f"After potion - Harry: {harry.current_health}, Draco: {draco.current_health}")

if __name__ == "__main__":
    main()