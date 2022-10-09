import pyautogui

class Player:

    key_cooldown = 1

    def __init__(self):
        return

    def move(self, direction):
        if direction == "s":
            pyautogui.press("s", self.key_cooldown)

        if direction == "n":
            pyautogui.press("w", self.key_cooldown)

        if direction == "e":
            pyautogui.press("d", self.key_cooldown)

        if direction == "w":
            pyautogui.press("a", self.key_cooldown)

        if direction == "nw":
            pyautogui.press("q", self.key_cooldown)

        if direction == "ne":
            pyautogui.press("e", self.key_cooldown)

        if direction == "sw":
            pyautogui.press("z", self.key_cooldown)

        if direction == "se":
            pyautogui.press("c", self.key_cooldown)