import pyautogui

im = pyautogui.screenshot()
print im.getpixel((860,1020))