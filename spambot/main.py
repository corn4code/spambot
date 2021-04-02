import pyautogui
import time
time.sleep(5)
for x in range(0,100):
    pyautogui.typewrite("Hello")
    pyautogui.press("Enter")

