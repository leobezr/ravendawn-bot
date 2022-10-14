from pickletools import read_bytes4
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer

pm = Pymem("ravendawn_dx-1665687500.exe")
game_module = module_from_name(pm.process_handle, "ravendawn_dx-1665687500.exe").lpBaseOfDll

def get_pointer(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    pointer_address = None

    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            pointer_address = remote_pointer.value + offset

    return pymem.Pymem.read_int(pm, pointer_address)