from lib.cavebot.waypoints import Waypoints
from lib.pointer import get_pointer, game_module
from lib.pathfinder import get_move_dir
from lib.player import player_instance
from lib.bot import bot_instance
from lib.cavebot.map import map_instance
from lib.utils import Utils
from threading import Thread
import keyboard
import time


MAX_DISTANCE_RANGE = 40
WALK_MAP_CLICKS = "map-click"
WALK_ARROWS = "arrow"
SQM_COLLISION_RADIUS = 1
LOG_STEPS = False


class Cavebot:
    _pos = (0, 0, 0)
    _bot = bot_instance
    _player = player_instance
    _map = map_instance

    _walk_method = WALK_MAP_CLICKS
    _last_pos = (0, 0, 0)
    _trapped = False

    collision_radius = SQM_COLLISION_RADIUS
    current_waypoint = None
    needle_position = 0
    is_on = False
    map_click = True

    def _update_pos(self):
        posX = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB1C])
        posY = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB20])
        posZ = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB24])

        self._pos = (posX, posY, posZ)
        return self._pos

    def _max_needle_position(self):
        if self.current_waypoint:
            return len(self.current_waypoint) - 1
        else:
            return 0

    def _next_needle_range(self):
        if self.needle_position < self._max_needle_position():
            self.needle_position += 1
        else:
            self.needle_position = 0

        Utils.log(f"Next waypoint: {self.current_waypoint[self.needle_position]}")

    def _previous_needle_range(self):
        Utils.log("Had to move one waypoint back")

        if self.needle_position > 0:
            self.needle_position -= 1
        else:
            self.needle_position = self._max_needle_position()

    def _get_target_pos(self):
        return self.current_waypoint[self.needle_position]

    def _orientation(self, selfOne, targetOne):
        if selfOne > targetOne:
            return "selfDecreasing"
        else:
            return "selfGrowing"

    def _is_valid_pos(self):
        x, y, z = self._update_pos()
        targetX, targetY, targetZ = self._get_target_pos()

        self._is_trapped((x, y, z))

        if z == targetZ:
            max_distance_range = MAX_DISTANCE_RANGE
            distanceX = abs(x - targetX)
            distanceY = abs(y - targetY)

            return distanceX < max_distance_range and distanceY < max_distance_range
        else:
            Utils.log(
                f"Invalid Z position, self position is {x} {y} {z}, target is {targetX} {targetY} {targetZ}"
            )
            self.pause()
            return False

    def _is_on_location(self):
        x, y, _ = self._update_pos()
        tarX, tarY, _ = self._get_target_pos()

        is_colliding = Utils.is_colliding(
            (x, y, 1), (tarX, tarY, self.collision_radius)
        )

        return is_colliding

    def _switch_walk_method(self):
        method = self._walk_method

        if method == WALK_MAP_CLICKS:
            self._walk_method = WALK_ARROWS
        else:
            self._walk_method = WALK_MAP_CLICKS

        Utils.log(f"Switch direction method to: {self._walk_method}")

    def _is_trapped(self, new_pos):
        trapped = new_pos == self._last_pos

        Utils.log(f"_is_trapped function: newPos: {new_pos}, old: {self._last_pos}")

        if trapped:
            self._switch_walk_method()
            Utils.log(
                f"Bot seems to be stuck, trying to shift {self._walk_method} method",
                LOG_STEPS,
            )

        self._last_pos = new_pos
        self._trapped = trapped

    def _move_towards_waypoint(self):
        x, y, _ = self._update_pos()
        tarX, tarY, _ = self._get_target_pos()

        if self._trapped:
            if self._walk_method == WALK_ARROWS:
                self._bot.move(
                    get_move_dir((x, y), (tarX, tarY), allowDiagonal=True, threshold=15)
                )
            else:
                self._map.click_map((x, y, _), (tarX, tarY, _))
        elif abs(x - tarX) > 3:
            self._map.click_map((x, y, _), (tarX, tarY, _))
        else:
            self._bot.move(
                get_move_dir((x, y), (tarX, tarY), allowDiagonal=True, threshold=15)
            )

    def __init__(self, filename):
        Utils.log("Cavebot has started")
        self.current_waypoint = Waypoints[filename]
        keyboard.add_hotkey("pause", self.pause)
        self.start()
        return

    def run(self):
        if self.is_on:
            if self._is_valid_pos():
                if not self._is_on_location():
                    self._move_towards_waypoint()
                else:
                    self._next_needle_range()
            else:
                self._previous_needle_range()

    def standalone_run(self):
        def run():
            while 1:
                self.run()
                time.sleep(.15)

        cavebotThread = Thread(target=run)
        cavebotThread.start()

    def pause(self):
        self.is_on = not self.is_on

        stage = "running" if self.is_on else "stopped"
        Utils.log(f"Cavebot {stage}")

    def start(self):
        self.is_on = True
