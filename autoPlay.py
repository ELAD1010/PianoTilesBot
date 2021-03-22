import pyautogui
import time
import win32api
import win32con
import keyboard

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("go")
while keyboard.is_pressed("q") == False:
    # if pyautogui.pixel(465,450)[0]==0: click(465,450)
    # if pyautogui.pixel(555,450)[0]==0: click(555,450)
    # if pyautogui.pixel(658,450)[0]==0: click(658,450)
    # if pyautogui.pixel(748,450)[0]==0: click(748,450)
      if pyautogui.pixel(740,1010)[0]==0: click(740,1010)
      if pyautogui.pixel(880,1010)[0]==0: click(880,1010)
      if pyautogui.pixel(1030,1010)[0]==0: click(1030,1010)
      if pyautogui.pixel(1155,1010)[0]==0: click(1155,1010)

    #520 y
    #0.1 sleep