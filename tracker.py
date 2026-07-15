import ctypes
from ctypes import wintypes
class LASTINPUTINFO(ctypes.Structure):
    _fields_=[("cbSize",wintypes.UINT),("dwTime",wintypes.DWORD)]
class IdleDetector:
    @staticmethod
    def get_idle_seconds():
        info=LASTINPUTINFO(); info.cbSize=ctypes.sizeof(info)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(info))
        return (ctypes.windll.kernel32.GetTickCount()-info.dwTime)/1000
