import pyautogui
import json
import time
import sys
import webbrowser


def classLogger(classid):
    url = 'https://zoom.us/j/'+str(classid)+'?from=join'
    webbrowser.open_new_tab(url)

    time.sleep(10)

    pyautogui.press('tab',presses=8)
    time.sleep(3)

    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.press('tab',presses=8)
    time.sleep(2)

    pyautogui.press('enter')


def initLogin():
    try:
        with open('data.txt') as rfile:
            data = json.load(rfile)

    except Exception as e:
        print('first import classid data from getdata.py')

    try:
        cString = 'class'+str(sys.argv[1])
        if(data[cString]):
            print("logging into class....")
            time.sleep(2)
            classLogger(data[cString])

    except Exception as e:
        print('no such class exists')



initLogin()
