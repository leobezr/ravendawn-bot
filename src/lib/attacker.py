from lib.yaml_reader import read_config
from lib.vision import vision_instance
from lib.anchors import Anchor
from lib.pointer import get_pointer, game_module
from threading import Thread
import pyautogui

TARGET_CIRCLE = Anchor.TARGET_CIRCLE
STAMINA_HOOK = Anchor.STAMINA_HOOK
LOG_ATTACKS = False

attacker_instance = None

STAMINA = {
    "10": 1076101120,
    "20": 1077149696,
    "30": 1077805056,
    "40": 1078198272,
    "50": 1078525952,
    "60": 1078853632,
    "70": 1079083008,
    "80": 1079246848,
    "90": 1079410688,
    "100": 1079574528
}

class Attacker:
    toolbar_position = [left, top, width, height] = read_config()["toolbar_position"]
    casting = False

    increase_stamina = read_config()["spells"]["increase_stamina"]
    needs_stamina = read_config()["spells"]["needs_stamina"]
    
    player_attacking = False

    def _snapshot_toolbar(self):
        [left, top, width, height] = self.toolbar_position
        return vision_instance.screenshot(left, top, width, height)

    def _sort_list(self, list):
        def return_priority(elem):
            return elem["priority"]
        
        list.sort(key=return_priority)

    def _use_spell(self, spell):
        pyautogui.press(spell["hotkey"], interval=.1)
    
    def _log(self, msg):
        if LOG_ATTACKS:
            print(msg)

    def __init__(self):
        self._sort_list(self.increase_stamina)
        self._sort_list(self.needs_stamina)

    def attack(self):
        if self.is_attacking():
            self.cast_spells()
        else:
            pyautogui.press("tab", interval=.6)
    
    def cast_spells(self):
        if self.has_stamina():
            for spell in self.needs_stamina:
                self._log("Using stamina spells")
                self._use_spell(spell)
                pyautogui.sleep(.05)

        else:
            for spell in self.increase_stamina:
                self._log("Recovering stamina")
                self._use_spell(spell)

    def is_attacking(self):
        target_id = get_pointer(game_module + 0x024BA568, [0xA18])
        self.player_attacking = target_id != 0
        
        return self.player_attacking

    def standalone_attack(self):
        def attack():
            while 1:
                self.attack()
                pyautogui.sleep(.01)

        targetThread = Thread(target=attack)
        targetThread.start()

    def has_stamina(self):
        stamina_amount = get_pointer(game_module + 0x024BAF90, [0x180, 0xC04])
        return stamina_amount >= STAMINA["50"]

if not attacker_instance:
    attacker_instance = Attacker()