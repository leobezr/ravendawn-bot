import pyautogui
import numpy as np
import cv2 as cv
import mss

DEBUG_MODE = False

threshold = 0.8
DEFAULT_CV2_METHOD = cv.TM_CCOEFF_NORMED
DEFAULT_CV2_BORDERCOLOR = (255, 0, 176)
vision_instance = None

class Vision:
    w, h = pyautogui.size()

    def __init__(self):
        return

    def get_target_hook(self, needle, levels, scene=None, threshold=.6, return_scene=False, label=False, crop=[0, 0, 0, 0], show_window=False):
        if scene is None:
            left, top, width, height = crop
            scene = self.screenshot(left, top, width, height)

        hsv_levels = self.hsv(scene, levels)

        if return_scene:
            return hsv_levels

        return self.find(needle, hsv_levels, threshold=threshold, label=label, show_window=show_window)


    def screenshot(self, left=0, top=0, width=0, height=0):
        stc = mss.mss()
        scr = stc.grab(
            {
                "left": left,
                "top": top,
                "width": width or self.w,
                "height": height or self.h,
            }
        )

        img = np.array(scr)
        img = cv.cvtColor(img, cv.IMREAD_COLOR)

        return img

    def mark_scene(self, size, position, scene, window_name):
        self.mark_target(size, position, scene)
        self.show(scene, window_name)

    def find(
        self,
        needle,
        scene_as_haystack,
        window_name="Bot",
        threshold=threshold,
        show_window=False,
        label=False,
        silent=False,
    ):
        result = cv.matchTemplate(scene_as_haystack, needle, DEFAULT_CV2_METHOD)
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            if not silent and label:
                print(f"Success: {max_val}, label: {label}")

            if DEBUG_MODE or show_window:
                needle_w, needle_h = (needle.shape[0], needle.shape[1])
                self.mark_scene((needle_w, needle_h), max_loc, scene_as_haystack, window_name)

            return True
        else:
            if DEBUG_MODE or label:
                print(f"Failed accuracy: {max_val}, Label: {label}, Expected threshold: {threshold}")
                self.show(scene_as_haystack)

            return False

    def find_position(self, needle, scene_as_haystack, threshold=threshold):
        result = cv.matchTemplate(scene_as_haystack, needle, DEFAULT_CV2_METHOD)
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val > threshold:
            print(f"Found position: {max_loc}")
            return max_loc
        else:
            print(f"Position not found! threshold: {threshold} | MaxVal: {max_val}")
            return (0, 0)

    def show(self, screenshot, window_name="Bot"):
        cv.imshow(window_name, screenshot)

    def mark_target(self, size, max_loc, screenshot):
        h, w = size
        x, y = max_loc
        color = DEFAULT_CV2_BORDERCOLOR

        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv.rectangle(
            screenshot, top_left, bottom_right, color, thickness=2, lineType=cv.LINE_8
        )

    def add_text(self, frame, message, position, color=(0, 0, 255)):
        return cv.putText(frame, message, position, cv.FONT_HERSHEY_SIMPLEX, 0.7, color)

    def add_rect(self, frame, position, size, color=(0, 0, 255)):
        return cv.rectangle(frame, position, size, color, thickness=2)

    # def target_circle_mask(self):
    #     return self._apply_mask(0, 222, 151, 5, 255, 255)

    def hsv(self, scene, levels):
        [h_min, s_min, v_min, h_max, s_max, v_max] = levels

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        # Convert to HSV format and color threshold
        hsv = cv.cvtColor(scene, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(scene, scene, mask=mask)

        return result


if not vision_instance:
    vision_instance = Vision()