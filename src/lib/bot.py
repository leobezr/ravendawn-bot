import pyautogui
from lib.core import get_game_client
from lib.player import Player
from lib.pathfinder import pathfinder

class Bot:

    client = None
    control = Player()
    
    win_w, win_h = pyautogui.size()
    center_w, center_h = (win_w / 2, win_h / 2)

    def __init__(self):
        print("Ravendawn Bot Started")
        self.client = get_game_client()

    def _get_mouse_pos(self):
        return pyautogui.position()

    def focus(self):
        self.client.maximize()
        self.client.activate()

    def move(self, direction):
        self.focus()
        self.control.move(direction)

    def chase_mouse(self):
        self.player.attacker.attack()

        if not self.attacker.casting:
            self.move(pathfinder())