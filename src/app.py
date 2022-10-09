from lib.yaml_reader import read_config
from lib.core import get_game_client
from lib.bot import Bot
import keyboard
import cv2 as cv

def __main__():
    print("Script initiated")
    
    game_bot = Bot()
    auto_path = True

    while True:
        if keyboard.read_key() == "ctrl":
            auto_path = not auto_path

        if auto_path:
            run_key_press_commands(game_bot)

        if cv.waitKey(1) == ord("q"):
            break

def run_key_press_commands(game_bot = Bot()):
    if keyboard.read_key() == "space":
        game_bot.chase_mouse()

if __name__ == "__main__":
    __main__()