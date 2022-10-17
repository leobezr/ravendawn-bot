from lib.threads.bot_chase import chase_mouse, chase_mouse_pause
from lib.threads.gathering import auto_gathering
from lib.devtools.devtools import Devtool
from lib.requirement_hooks import *
from lib.cavebot.cavebot import Cavebot
from lib.devtools.waypoint_creator import WaypointCreator
from lib.utils import Utils
import keyboard
import cv2 as cv

def __main__():
    Utils.log("")
    Utils.log("Bezr Bot has started!")
    
    dev_mode = False
    manual_mode = True
    waypoint_mode = False
    script_running = 1

    devtool = Devtool(dev_mode)
    cavebot = Cavebot("ravencrest")
    waypoint = WaypointCreator("ravencrest")

    if manual_mode:
        Utils.log("Bot is running in Manual Mode")

    if waypoint_mode:
        Utils.log("Bot is running in Waypoint Mode")

    while script_running:
        if dev_mode:
            devtool.get_stamina()

        elif waypoint_mode:
            key = cv.waitKey(1)

            if key == ord("q"):
                cv.destroyAllWindows()
                break

            if keyboard.read_key() == "+":
                waypoint.register()

            elif keyboard.read_key() == "-":
                waypoint.remove_last()

            elif keyboard.read_key() == "insert":
                waypoint.save()

        elif manual_mode:
            if keyboard.read_key() == "space":
                chase_mouse()

            if keyboard.read_key() == "pause":
                chase_mouse_pause()

        else:

            cavebot.start()

if __name__ == "__main__":
    __main__()