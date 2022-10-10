from lib.vision import Vision
from lib.devtools.trackbar import Trackbar
import cv2 as cv

class Devtool:
    scene = None
    vision = Vision()
    trackbar = Trackbar()

    def __init__(self):
        return

    def _screenshot(self):
        self.scene = self.vision.screenshot()

    def use_trackbars(self, scene):
        self.trackbar.update(scene)
        cv.imshow("bla", self.trackbar.result)

    def show(self, scene):
        self.vision.show()

    def run_visual_test(self, needle, scene, window_name="Devtool scene", threshold=0.8):
        self._screenshot()
        
        if not scene:
            scene = self.scene

        self.scene = self.vision.find(needle, scene, window_name, threshold)