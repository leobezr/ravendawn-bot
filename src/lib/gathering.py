from lib.anchors import Anchor
from lib.vision import vision_instance
from lib.yaml_reader import read_config
from lib.masks import Masks
import pyautogui
import time
import cv2 as cv

ANCHOR = Anchor.GATHERING_ANCHOR
NEEDLE = Anchor.GATHERING_NEEDLE
[left, top, width, height] = read_config()["gathering_position"]

TIMEOUT = 1000 * 10

class Gathering:

    timeout = 0
    scene = None

    def _now(self):
        return time.time_ns() // 1_000_000

    def _screenshot(self):
        self.scene = vision_instance.screenshot(left, top, width, height)

    def __init__(self):
        self._screenshot()
        return

    def is_gathering(self):
        self._screenshot()
        return vision_instance.get_target_hook(ANCHOR, Masks.GATHERING, threshold=.89, scene=self.scene, show_window=True)

    def _auto_gather(self):
        self._screenshot()
        
        if vision_instance.get_target_hook(NEEDLE, Masks.GATHERING_NEEDLE, threshold=.7, scene=self.scene, show_window=True, label="Needle"):
            pyautogui.press("f")

    def gather(self):
        if self._now() < self.timeout:
            self._auto_gather()
        elif self.is_gathering():
            print("Setting new timeout")
            self.timeout = self._now() + TIMEOUT
    