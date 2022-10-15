from lib.bot import bot_instance
import threading

bot = bot_instance

def auto_targeting():
    mouse_chase_thread = threading.Thread(target=bot.chase_mouse)
    targeting_thread = threading.Thread(target=bot.attack)

    mouse_chase_thread.start()
    targeting_thread.start()