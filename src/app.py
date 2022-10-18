from lib.threads.bot_chase import chase_mouse, chase_mouse_pause
from lib.devtools.devtools import Devtool
from lib.requirement_hooks import *
from lib.cavebot.cavebot import Cavebot
from lib.devtools.waypoint_creator import WaypointCreator
from lib.attacker import attacker_instance
from lib.utils import Utils
from bot_modes import BotMode
import keyboard
import cv2 as cv


def __main__():
    Utils.log("")
    Utils.log("Bezr Bot has started!")

    # BOT SETTINGS
    BOT_MODE = BotMode.cavebot
    #

    devtool = Devtool(BOT_MODE == BotMode.dev)
    waypoint = WaypointCreator("desert_turtles")

    if BOT_MODE == BotMode.manual:
        Utils.log("Bot is running in Manual Mode")

    elif BOT_MODE == BotMode.waypointCreator:
        Utils.log("Bot is running in Waypoint Mode")

    elif BOT_MODE == BotMode.cavebot:
        cavebot = Cavebot("desert_turtles")
        attacker_instance.standalone_attack()
        cavebot.standalone_run()

    while 1:
        if BOT_MODE == BotMode.dev:
            devtool.health()

        elif BOT_MODE == BotMode.waypointCreator:
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

        elif BOT_MODE == BotMode.manual:
            if keyboard.read_key() == "space":
                chase_mouse()

            if keyboard.read_key() == "pause":
                chase_mouse_pause()

if __name__ == "__main__":
    __main__()