from lib.vision import vision_instance
from lib.devtools.trackbar import Trackbar
from lib.attacker import attacker_instance
from lib.yaml_reader import read_config
import cv2 as cv

class Devtool:
    scene = None
    vision = vision_instance
    trackbar = Trackbar()
    attacker = attacker_instance

    toolbar_position = [left, top, width, height] = read_config()["toolbar_position"]

    def __init__(self):
        return

    def _screenshot(self):
        self.scene = self.vision.screenshot()

    def use_trackbars(self, scene):
        self.trackbar.update(scene)
        cv.imshow("bla", self.trackbar.result)

    def find_hook(self, hook, scene, level):
        if scene is None:
            scene = vision_instance.screenshot()

        scene = vision_instance.get_target_hook(hook, level, scene=scene, threshold=.98, label="Spell")

    def snapshot_toolbar(self):
        return self.vision.screenshot(self.left, self.top, self.width, self.height)


    def show(self, scene):
        self.vision.show()

    def run_visual_test(self, needle, scene, window_name="Devtool scene", threshold=0.8):
        self._screenshot()
        
        if not scene:
            scene = self.scene

        self.scene = self.vision.find(needle, scene, window_name, threshold)