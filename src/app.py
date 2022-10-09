from lib.yaml_reader import read_config
from lib.core import get_game_client
from lib.bot import Bot
import keyboard
import cv2 as cv

def __main__():
    print("Script initiated")
    start_bot_loop()

def start_bot_loop():
    print("Starting game loop")
    # config = read_config()
    
    game_bot = Bot()

    while True:

        if keyboard.read_key() == "space":
            game_bot.chase_mouse()

        if cv.waitKey(1) == ord("q"):
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    __main__()