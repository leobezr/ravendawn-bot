from lib.bot import Bot
import keyboard
import threading

bot = Bot()

def auto_targeting():
    if keyboard.read_key() == "pause":
        mouse_chase_thread = threading.Thread(target=bot.chase_mouse)
        targeting_thread = threading.Thread(target=bot.attack)

        mouse_chase_thread.start()
        targeting_thread.start()