import subprocess
from time import sleep
import pyautogui as gui
from PIL import Image

if __name__=='__main__':

  icon_p = "./images/dmm.png"
  x = gui.locateCenterOnScreen(icon_p, confidence=0.9)
  print(x)

  # proc = subprocess.Popen('C:\\Program Files (x86)\\Nox\\bin\\Nox.exe')
  # sleep(60)
  # x, y = gui.locateCenterOnScreen(icon_p, confidence=0.9)
  # print(x, y)
  # proc.terminate()
  