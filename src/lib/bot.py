import pyautogui
from lib.core import get_game_client
from lib.player import player_instance
from lib.pathfinder import pathfinder


class Bot:

    client = None
    player = player_instance

    win_w, win_h = pyautogui.size()
    center_w, center_h = (win_w / 2, win_h / 2)

    def __init__(self):
        self.client = get_game_client()

    def _get_mouse_pos(self):
        return pyautogui.position()

    def focus(self):
        self.client.maximize()
        self.client.activate()

    def move(self, direction):
        self.focus()
        self.player.move(direction)

    def attack(self):
        self.player.attack()

    def chase_mouse(self):
        self.attack()
        
        if not self.player.get_is_casting():
            self.move(pathfinder())


bot_instance = None

if not bot_instance:
    bot_instance = Bot()
