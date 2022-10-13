from lib.vision import vision_instance
from lib.devtools.trackbar import Trackbar
from lib.attacker import attacker_instance
from lib.yaml_reader import read_config
from lib.masks import Masks
import cv2 as cv


SCENE = cv.imread(r".\src\__mocks__\scene\attack_position\attack-on-dark.jpg")
NEEDLE = cv.imread(r".\src\target\attack-position\min-stamina_v4.jpg")

class Devtool:
    scene = None
    vision = vision_instance
    trackbar = Trackbar()
    attacker = attacker_instance

    toolbar_position = [left, top, width, height] = read_config()["toolbar_position"]

    def __init__(self, is_on):
        if is_on:
            self.set_env()

        return

    def _screenshot(self):
        self.scene = self.vision.screenshot()
        return self.scene

    def set_env(self):
        self.trackbar.start_up(110, 80, 71, 144, 248, 255)

    def use_trackbars(self, scene):
        self.trackbar.update(scene)
        cv.imshow("bla", self.trackbar.result)

    def find_hook(self, hook, scene, level, threshold=.98):
        if scene is None:
            scene = vision_instance.screenshot()

        scene = vision_instance.get_target_hook(hook, level, scene=scene, threshold=threshold, label="Spell")

    def snapshot_toolbar(self):
        return self.vision.screenshot(self.left, self.top, self.width, self.height)
    
    def test(self, use_trackbars=False):
        if use_trackbars:
            self.use_trackbars(self.snapshot_toolbar())
        else:
            self.find_hook(NEEDLE, self.snapshot_toolbar(), Masks.STAMINA, threshold=.49)

    def show(self, scene):
        self.vision.show()