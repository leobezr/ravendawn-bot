from pickletools import read_bytes4
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer

pm = Pymem("ravendawn_dx-1666037946.exe")
game_module = module_from_name(pm.process_handle, "ravendawn_dx-1666037946.exe").lpBaseOfDll

def get_pointer(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    pointer_address = None

    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            pointer_address = remote_pointer.value + offset

    return pymem.Pymem.read_int(pm, pointer_address)

def mana_percent():
    return get_pointer(game_module + 0x024BB9F0, [0x0, 0x158, 0x1E0])

def health_percent():
    return get_pointer(game_module + 0x024BB9F0, [0x0, 0x158, 0x88])

def position():
    posX = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB1C])
    posY = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB20])
    posZ = get_pointer(game_module + 0x024BB0C8, [0x40, 0xB24])

    return (posX, posY, posZ)

def stamina_amount():
    return get_pointer(game_module + 0x024BAF90, [0x180, 0xC04])

def is_attacking():
    target_id = get_pointer(game_module + 0x024BA568, [0xA18])
    return target_id != 0