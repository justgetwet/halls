import subprocess
from time import sleep
import pyautogui as gui
import win32gui
import pyperclip
from PIL import Image, ImageGrab

if __name__=='__main__':

  dmm_icon = "./images/dmm.png"
  mypage_icon = "./images/mypage.png"
  dstation_icon = "./images/dstation.png"
  data_icon = "./images/datakokai.png"
  search_icon = "./images/search_no.png"
  star_icon = "./images/yellow_star.png"
  
  nox = "C:\\Program Files (x86)\\Nox\\bin\\Nox.exe"

  proc = subprocess.Popen(nox)
  sleep(60)
  dmm_pos = None
  while dmm_pos is None:
    dmm_pos = gui.locateCenterOnScreen(dmm_icon, confidence=0.9)
    sleep(5)
  gui.click(dmm_pos)
  sleep(20)
  
  mypage_pos = None
  while mypage_pos is None:
    mypage_pos = gui.locateCenterOnScreen(mypage_icon, confidence=0.9)
    sleep(5)
  gui.click(mypage_pos)
  sleep(20)
  
  ds_pos = None
  while ds_pos is None:
    ds_pos = gui.locateCenterOnScreen(dstation_icon, confidence=0.9)
    sleep(5)
  gui.click(ds_pos)
  sleep(20)
  
  data_pos = None
  while data_pos is None:
    data_pos = gui.locateCenterOnScreen(data_icon, confidence=0.9)
    sleep(5)
  gui.click(data_pos)
  sleep(20)
  
  search_pos = None
  while search_pos is None:
    search_pos = gui.locateCenterOnScreen(search_icon, confidence=0.9)
    sleep(5)
  gui.click(search_pos)
  sleep(1)
  machine_no = 1
  pyperclip.copy(machine_no)
  gui.hotkey("ctrl", "v")
  sleep(1)
  gui.hotkey("return")
  sleep(20)
  
  star_pos = None
  while star_pos is None:
    star_pos = gui.locateCenterOnScreen(star_icon, confidence=0.9)
    sleep(5)
  
  x, y = star_pos
  gui.moveTo(x + 100, y + 100)
  sleep(5)
  gui.dragRel(0, -450, duration=1, button='left')
  sleep(5)
  handle = win32gui.FindWindow(None, 'NoxPlayer')
  rect = win32gui.GetWindowRect(handle)
  img = ImageGrab.grab(rect)
  print(img.size)
  
  proc.terminate()
  