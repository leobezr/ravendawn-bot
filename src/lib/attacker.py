from lib.yaml_reader import read_config
from lib.vision import vision_instance
from lib.masks import Masks
from lib.anchors import Anchor, get_link
import pyautogui

TARGET_CIRCLE = Anchor.TARGET_CIRCLE
STAMINA_HOOK = Anchor.STAMINA_HOOK
LOG_ATTACKS = False

attacker_instance = None

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

    def _use_spell(self, spell, scene):
        if vision_instance.get_target_hook(spell["target_anchor"], Masks.SPELLS, threshold=.9, scene=scene):
            if spell["needs_casting"]:
                self.casting = True
                pyautogui.sleep(1)

                pyautogui.press(spell["hotkey"])
                pyautogui.sleep(spell["needs_casting"])
                self._log(f"Pressed {spell['hotkey']} key")
            else:
                self.casting = False

                pyautogui.press(spell["hotkey"])
                self._log(f"Pressed {spell['hotkey']} key")
                pyautogui.sleep(1)
    
    def _log(self, msg):
        if LOG_ATTACKS:
            print(msg)

    def __init__(self):
        self._sort_list(self.increase_stamina)
        self._sort_list(self.needs_stamina)

        for spell in self.increase_stamina:
            spell["target_anchor"] = get_link(spell["target_anchor"])

        for spell in self.needs_stamina:
            spell["target_anchor"] = get_link(spell["target_anchor"])

    def attack(self, is_walking):
        if self.is_attacking():
            self.cast_spells(is_walking)
        else:
            pyautogui.press("tab")
    
    def cast_spells(self, is_walking):
        scene = self._snapshot_toolbar()

        if self.has_stamina():
            for spell in self.needs_stamina:
                self._log("Using stamina spells")
                self._use_spell(spell, scene)

        else:
            for spell in self.increase_stamina:
                self._log("Recovering stamina")
                self._use_spell(spell, scene)

    def is_attacking(self):
        self.player_attacking = vision_instance.get_target_hook(TARGET_CIRCLE, Masks.TARGET_CIRCLE, threshold=.36)
        return self.player_attacking

    def has_stamina(self):
        return vision_instance.get_target_hook(STAMINA_HOOK, Masks.STAMINA, threshold=.49, crop=self.toolbar_position)

if not attacker_instance:
    attacker_instance = Attacker()