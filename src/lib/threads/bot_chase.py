from lib.bot import bot_instance
from lib.utils import Utils
from threading import Thread

class BotChase:
    is_on = False
    bot = bot_instance

    def _chase_mouse(self):
        if self.is_on:
            self.bot.chase_mouse()

    def _auto_attack(self):
        if self.is_on:
            self.bot.attack()

    def __init__(self):   
        self.is_on = True

    def run(self):
        movementThread = Thread(target=self._chase_mouse)
        movementThread.start()

    def pause(self):
        self.is_on = not self.is_on                 
        Utils.log(f"Paused set: {self.is_on}")


bot_chase = BotChase()

def chase_mouse():
    bot_chase.run()

def chase_mouse_pause():
    bot_chase.pause()