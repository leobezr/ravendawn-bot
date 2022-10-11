import pyautogui

PROCESS_NAME = "Ravendawn -"

def get_game_client():
    return pyautogui.getWindowsWithTitle(PROCESS_NAME)[0] 