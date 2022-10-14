from lib.gathering import Gathering
import threading

gathering = Gathering()

def auto_gathering():
    auto_gather_thread = threading.Thread(target=gathering.gather)
    auto_gather_thread.start()
