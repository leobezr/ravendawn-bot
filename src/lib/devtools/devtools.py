from lib.vision import vision_instance
from lib.devtools.trackbar import Trackbar
from lib.attacker import attacker_instance
from lib.yaml_reader import read_config
from lib.masks import Masks
from lib.pointer import get_pointer, game_module
import time
import cv2 as cv


SCENE = cv.imread(r".\src\__mocks__\scene\gathering\gathering.jpg")
NEEDLE = cv.imread(r".\src\target\gathering\gathering-needle.jpg")

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
        self.trackbar.start_up(0, 0, 0, 179, 255, 255)

    def use_trackbars(self, scene):
        self.trackbar.update(scene)
        cv.imshow("bla", self.trackbar.result)

    def find_hook(self, hook, scene, level, threshold=.98):
        if scene is None:
            scene = vision_instance.screenshot()

        scene = vision_instance.get_target_hook(hook, level, scene=scene, threshold=threshold, label="Spell", show_window=True)

    def snapshot_toolbar(self):
        return self.vision.screenshot(self.left, self.top, self.width, self.height)

    def snapshot_gathering(self):
        [left, top, width, height] = read_config()["gathering_position"]
        return self.vision.screenshot(left, top, width, height)
    
    def test(self, use_trackbars=False):
        if use_trackbars:
            self.use_trackbars(SCENE)
        else:
            self.find_hook(NEEDLE, self.snapshot_gathering(), Masks.GATHERING_NEEDLE, threshold=.7)

    def print_waypoint(self):
        posX = get_pointer(game_module + 0x024BB0A8, [0x40, 0xB1C])
        posY = get_pointer(game_module + 0x024BB0A8, [0x40, 0xB20])
        posZ = get_pointer(game_module + 0x024BB0A8, [0x40, 0xB24])

        print(posX, posY, posZ)


    def show(self, scene):
        self.vision.show()