from lib.yaml_reader import get_root_dir
import matplotlib.pyplot as plt 
import cv2 as cv

def get_link(path):
    return cv.imread(get_root_dir() + path)

class Anchor:

    TARGET_CIRCLE = get_link(r"\target\attack-position\target-circle.jpg")
    STAMINA_HOOK = get_link(r".\target\attack-position\min-stamina.jpg")

    GATHERING_ANCHOR = get_link(r".\target\gathering\gathering-anchor.jpg")
    GATHERING_NEEDLE = get_link(r".\target\gathering\gathering-needle.jpg")