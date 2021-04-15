import webbrowser
import pyautogui
import time

print('initial signing into zoom')

url = 'https://zoom.us'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

time.sleep(8)

pyautogui.press('tab',presses=12)
time.sleep(5)

pyautogui.press('enter')

time.sleep(5)

for i in range(0,8):
    pyautogui.press('tab')
    time.sleep(1)

time.sleep(3)

pyautogui.press('enter')
