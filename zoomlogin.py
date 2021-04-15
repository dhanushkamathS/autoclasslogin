import webbrowser
import pyautogui
import time

url = 'https://zoom.us'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

time.sleep(5)

pyautogui.press('tab',presses=12)
time.sleep(2)

pyautogui.press('enter')

time.sleep(3)

pyautogui.press('tab',presses=8)
time.sleep(2)

pyautogui.press('enter')