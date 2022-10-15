import math


class UtilsHelper:
    def __init__(self):
        return

    def is_colliding(self, posOne, posTwo):
        x1, y1, r1 = posOne
        x2, y2, r2 = posTwo

        dx = x1 - x2
        dy = y1 - y2

        distance = math.sqrt((dx * dx) + (dy * dy))

        colliding = distance < r1 + r2
        return colliding

    def log(self, msg, logSteps=True):
        if logSteps:
            print(msg)
            print("====================================================")


Utils = None

if not Utils:
    Utils = UtilsHelper()
