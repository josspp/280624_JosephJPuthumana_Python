import os
import win32api
import win32con
import win32gui
import ctypes

def SetWallpaper(image_path):
# The SPI_SETDESKWALLPAPER command is used to set the wallpaper
    # 0x0014 corresponds to SPI_SETDESKWALLPAPER, and 0x02 means to use the wallpaper style (fit)
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    # Call the SystemParametersInfo API
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

SetWallpaper("Image1.jpg")