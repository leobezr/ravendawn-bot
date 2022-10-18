from lib.pointer import get_pointer, game_module
from lib.yaml_reader import get_cavebot_waypoint, save_file
import time

class WaypointCreator:
    waypoint_name = ""
    waypoints = []

    def __init__(self, waypoint_name):
        self.waypoint_name = waypoint_name
        self.waypoints = get_cavebot_waypoint(waypoint_name)
        
        if self.waypoints[0] is None:
            self.remove_last()

    def register(self):
        posX = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB1C])
        posY = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB20])
        posZ = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB24])

        if not any(wpt == (posX, posY, posZ) for wpt in self.waypoints):
            self.waypoints.append((posX, posY, posZ))
            print(self.waypoints)
            time.sleep(.1)

    def remove_last(self):
        self.waypoints.pop()
        print(self.waypoints)
        time.sleep(.2)

    def save(self):
        save_file(self.waypoint_name, self.waypoints)