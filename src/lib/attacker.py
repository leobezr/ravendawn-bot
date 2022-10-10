from lib.yaml_reader import read_config

class Attacker:
    spells_config = read_config()["spells"]
    casting = False

    print(spells_config)

    def __init__(self):
        return

    def attack(self):
        return

    def is_attacking(self):
        return False

    def has_stamina(self):
        return False

    def use_spell_increase_stamina(self):
        return