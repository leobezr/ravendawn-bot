from lib.threads.bot import auto_targeting
from lib.devtools.devtools import Devtool
import keyboard
import cv2 as cv
import time


def __main__():
    print("Script initiated")
    
    dev_mode = False
    auto_path = True
    loop = 1
    devtool = Devtool(dev_mode)

    while loop:

        if dev_mode:
            key = cv.waitKey(1)
            devtool.test(use_trackbars=False)

            if key == ord("q"):
                cv.destroyAllWindows()
                break
        else:
            if auto_path:
                run_key_press_commands()

            if keyboard.read_key() == "pause":
                auto_path = not auto_path
                print(f"Auto path is set to {auto_path}")
                time.sleep(.2)

            if keyboard.read_key() == "end":
                print("Bot loop stopped")
                loop = False
                time.sleep(.2)
                break

def run_key_press_commands():
    if keyboard.read_key() == "space":
        auto_targeting()

if __name__ == "__main__":
    __main__()