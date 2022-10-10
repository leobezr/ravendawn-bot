from lib.bot import Bot
from lib.devtools.devtools import Devtool
import keyboard
import cv2 as cv
import time

# SCENE = cv.imread(r".\src\__mocks__\scene\attack_position\attacking-right.jpg")
# NEEDLE = cv.imread(r".\src\target\attack-position\attacking-right.png")

def __main__():
    print("Script initiated")
    
    dev_mode = False
    auto_path = True
    game_bot = Bot()
    devtool = Devtool()

    if dev_mode:
        devtool.trackbar.start_up()

    while True:

        if auto_path:
            run_key_press_commands(game_bot)

        if keyboard.read_key() == "ctrl":
            auto_path = not auto_path
            time.sleep(.3)
        
        if dev_mode:
            key = cv.waitKey(1)
            devtool.use_trackbars(SCENE)

            if key == ord("q"):
                cv.destroyAllWindows()
                break

def run_key_press_commands(game_bot = Bot()):
    if keyboard.read_key() == "space":
        game_bot.chase_mouse()

if __name__ == "__main__":
    __main__()