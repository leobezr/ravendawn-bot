import pyautogui
from lib.yaml_reader import read_config
from lib.attacker import attacker_instance

hotkeys = read_config()["hotkeys"]["movement"]

class Player:

    attacker = attacker_instance
    key_cooldown = .6
    walking = False

    def __init__(self):
        return

    def _press(self, direction):
        self.walking = True
        pyautogui.keyDown(direction)
        pyautogui.sleep(self.key_cooldown)
        pyautogui.keyUp(direction)
        self.walking = False

    def get_is_casting(self):
        return self.attacker.casting

    def attack(self):
        self.attacker.attack(self.walking)

    def is_attacking(self):
        return self.attacker.is_attacking()

    def move(self, direction):
        if direction == "s":
            self._press(hotkeys["south"])

        if direction == "n":
            self._press(hotkeys["north"])

        if direction == "e":
            self._press(hotkeys["east"])

        if direction == "w":
            self._press(hotkeys["west"])

        if direction == "nw":
            self._press(hotkeys["north_west"])

        if direction == "ne":
            self._press(hotkeys["north_east"])

        if direction == "sw":
            self._press(hotkeys["south_west"])

        if direction == "se":
            self._press(hotkeys["south_east"])

player_instance = None

if not player_instance:
    player_instance = Player()