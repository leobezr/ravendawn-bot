from lib.threads.bot import auto_targeting
from lib.threads.gathering import auto_gathering
from lib.devtools.devtools import Devtool
import keyboard
import cv2 as cv
import time


def __main__():
    print("Script initiated")
    
    dev_mode = True
    auto_path = True
    loop = 1
    devtool = Devtool(dev_mode)

    while loop:
        key = cv.waitKey(1)
        if key == ord("q"):
            cv.destroyAllWindows()
            break

        if dev_mode:
            # devtool.test(use_trackbars=False)
            devtool.test_pointers()

        else:
            if auto_path:
                auto_gathering()
                auto_targeting()

            if keyboard.read_key() == "pause":
                auto_path = not auto_path
                print(f"Auto path is set to {auto_path}")
                time.sleep(.2)

            if keyboard.read_key() == "end":
                print("Bot loop stopped")
                loop = False
                time.sleep(.2)
                break

if __name__ == "__main__":
    __main__()