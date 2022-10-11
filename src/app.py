from lib.bot import Bot
from lib.devtools.devtools import Devtool
import keyboard
import cv2 as cv
import time
import threading

from lib.masks import Masks


def __main__():
    print("Script initiated")
    
    dev_mode = False
    auto_path = True
    game_bot = Bot()
    devtool = Devtool()

    if dev_mode:
        devtool.trackbar.start_up()

    while 1:

        if dev_mode:
            key = cv.waitKey(1)
            # devtool.use_trackbars(STAMINA_MEDIUM)
            scene = devtool.snapshot_toolbar()
            devtool.find_hook(STAMINA, scene, Masks.STAMINA)
            

            if key == ord("q"):
                cv.destroyAllWindows()
                break
        else:
            if auto_path:
                run_key_press_commands(game_bot)

            if keyboard.read_key() == "ctrl":
                auto_path = not auto_path
                print(f"Auto path is set to {auto_path}")
                time.sleep(.3)

def run_key_press_commands(game_bot = Bot()):
    if keyboard.read_key() == "space":
        mouse_chaser_thread = threading.Thread(target=game_bot.chase_mouse)
        attack_handler_thread = threading.Thread(target=game_bot.attack)

        mouse_chaser_thread.start()
        attack_handler_thread.start()

if __name__ == "__main__":
    __main__()