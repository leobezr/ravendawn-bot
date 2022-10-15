import math
import pyautogui

win_w, win_h = pyautogui.size()
cx, cy = (win_w / 2, win_h / 2)
true_north = 90
true_west = 0
true_east = 180

THRESHOLD = 20


def _get_mouse_pos():
    return pyautogui.position()


def _to_degree(value):
    return int(value * (180 / math.pi))


def _get_tilt_direction(degree=0, allowDiagonal=True, threshold=THRESHOLD):
    is_pointing_up = degree > 0
    degree = abs(degree)

    if not allowDiagonal:
        threshold = 50

    if degree >= true_north + threshold:
        if degree >= true_east - threshold:
            return "e"
        else:
            if is_pointing_up:
                return "ne"
            else:
                return "se"

    elif degree <= true_north - threshold:
        if degree >= true_west + threshold:
            if is_pointing_up:
                return "nw"
            else:
                return "sw"
        else:
            return "w"
    elif is_pointing_up:
        return "n"
    else:
        return "s"


def pathfinder():
    x, y = _get_mouse_pos()

    degree = _to_degree(math.atan2(cy - y, cx - x))

    return _get_tilt_direction(degree=degree)


def get_degree(selfPos, targetPos, diameter=0):
    selfX, selfY = selfPos
    targetX, targetY = targetPos

    return _to_degree(math.atan2(selfY - targetY, selfX - targetX))

def get_move_dir(selfPos, targetPos, allowDiagonal=True, threshold=20):
    degree = get_degree(selfPos, targetPos)
    return _get_tilt_direction(degree=degree, allowDiagonal=allowDiagonal, threshold=threshold)
