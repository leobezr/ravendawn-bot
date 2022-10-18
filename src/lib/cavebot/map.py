from lib.yaml_reader import read_config
from lib.bot import bot_instance
from lib.utils import Utils
import pyautogui
import time

map_position = read_config()["map_position"]
MS_PER_SQM = .18
SQM_SIZE = 2
LOG_STEPS = False


class Map:
    _bot = bot_instance
    map_offset_x, map_offset_y, map_width, map_height = map_position

    def _dist_time(self, selfPos, targetPos):
        x1, y1, _ = selfPos
        x2, y2, _ = targetPos

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        time_to_walk_distance = (dx + dy) * MS_PER_SQM
        Utils.log(f"Walking time: {time_to_walk_distance}", LOG_STEPS)

        return time_to_walk_distance

    def _bisect_map_coord(self, selfPos, targetPos):
        x1, y1, _ = selfPos
        x2, y2, _ = targetPos

        Utils.log(f"My positions, selfPos: {selfPos} and targetPos: {targetPos}", LOG_STEPS)

        mx, my = self.map_offset_x, self.map_offset_y

        dx = x1 - x2
        dy = y1 - y2

        Utils.log(f"SQM difference, DX: {dx} and DY: {dy}", LOG_STEPS)

        cx = mx - (dx * SQM_SIZE)
        cy = my - (dy * SQM_SIZE)

        Utils.log(f"Click coord, CX: {cx} and CY: {cy}", LOG_STEPS)
        return (cx, cy)

    def __init__(self):
        return

    def click_map(self, selfPos, targetPos):
        x, y = self._bisect_map_coord(selfPos, targetPos)
        self._bot.focus()

        pyautogui.click(x, y)
        time.sleep(self._dist_time(selfPos, targetPos))


map_instance = None

if not map_instance:
    map_instance = Map()
