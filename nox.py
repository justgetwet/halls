import subprocess
from time import sleep
import pyautogui as gui
import win32gui
import pyperclip
from PIL import Image, ImageGrab
import datetime
import json
import sys
import io
import pyocr
import pyocr.builders

# sys.stdout = io.TextIOWrapper(
  # sys.stdout.buffer, encoding=sys.stdout.encoding, errors="replace"
# )

class Ocr:
  
  def scan(self, img) -> str:
  
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    
    tool = tools[0]
    txt = tool.image_to_string(
        img,
        lang="jpn+eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    return txt

class DmmCrawl(Ocr):
  
  nox_p = "C:\\Program Files (x86)\\Nox\\bin\\Nox.exe"
  
  def openDmm(self) -> subprocess.Popen:
  
    dmm_icon = "./images/dmm.png"
    mypage_icon = "./images/mypage.png"
    dstation_icon = "./images/dstation.png"
  
    proc = subprocess.Popen(self.nox_p)
    sleep(60)
    
    dmm_pos = None
    while dmm_pos is None:
      dmm_pos = gui.locateCenterOnScreen(dmm_icon, confidence=0.9)
      sleep(5)
    gui.click(dmm_pos)
    sleep(10)

    mypage_pos = None
    while mypage_pos is None:
      mypage_pos = gui.locateCenterOnScreen(mypage_icon, confidence=0.9)
      sleep(5)
    gui.click(mypage_pos)
    sleep(5)

    ds_pos = None
    while ds_pos is None:
      ds_pos = gui.locateCenterOnScreen(dstation_icon, confidence=0.9)
      sleep(5)
    gui.click(ds_pos)
    sleep(10)
    
    return proc
    
  def ocr_process(self, img):
  
    hits_box = (200, 340, 275, 400)
    continue_box = (200, 410, 275, 470)
    games_box = (200, 550, 275, 610)
    prv_box = (340, 625, 415, 685)
    
    hits_crop = img.crop(hits_box)
    continue_crop = img.crop(continue_box)
    games_crop = img.crop(games_box)
    prv_crop = img.crop(prv_box)
    
    hits = self.scan(hits_crop)
    continues = self.scan(continue_crop)
    games = self.scan(games_crop)
    prvGames = self.scan(prv_crop)
    
    return hits, continues, games, prvGames

  def machine(self, no: int, machine: str):
  
    data_icon = "./images/data_kokai.png"
    search_icon = "./images/search_no.png"
    star_icon = "./images/yellow_star.png"
    x_icon = "./images/x.png"
    img_p = "./im.png"
    
    data_pos = None
    while data_pos is None:
      data_pos = gui.locateCenterOnScreen(data_icon, confidence=0.9)
      sleep(5)
    gui.click(data_pos)
    sleep(10)
  
    search_pos = None
    while search_pos is None:
      search_pos = gui.locateCenterOnScreen(search_icon, confidence=0.9)
      sleep(5)
    gui.click(search_pos)
    sleep(5)
    # machine_no = no
    pyperclip.copy(no)
    gui.hotkey("ctrl", "v")
    sleep(1)
    gui.hotkey("return")
    sleep(10)

    star_pos = None
    while star_pos is None:
      star_pos = gui.locateCenterOnScreen(star_icon, confidence=0.9)
      sleep(5)

    x, y = star_pos
    gui.moveTo(x + 100, y + 500)
    sleep(5)
    gui.dragRel(0, -450, duration=1, button='left')
    sleep(5)
    handle = win32gui.FindWindow(None, 'NoxPlayer')
    rect = win32gui.GetWindowRect(handle)
    img = ImageGrab.grab(rect)
    tpl = self.ocr_process(img)
    dt_now = datetime.datetime.now()
    dt = dt_now.strftime('%m/%d %H:%M')
    dic = {no: [machine, dt] + list(tpl)}
    sleep(5)

    x_pos = None
    while x_pos is None:
      x_pos = gui.locateCenterOnScreen(x_icon, confidence=0.9)
      sleep(5)
    gui.click(x_pos)
    sleep(5)
    
    return dic

def is_num(self, str_num):
  try:
    float(str_num)
  except ValueError:
    return False
  else:
    return True

if __name__=='__main__':

  p = "./ds.json"
  with open(p, "r", encoding="utf-8") as f:
    read_dic = json.load(f)
  
  
  # txt = ocr.scan(im)
  # print(txt)
  crawl = DmmCrawl()
  proc = crawl.openDmm()
  works = {}
  for key, item in read_dic.items():
    dic = crawl.machine(int(key), item)
    works.update(dic)
  proc.terminate()
  print(works)
  
  read_json = json.dumps(works, ensure_ascii=False)
  p_w = "./ds_works.json"
  with open(p_w, "w", encoding="utf-8") as f:
    f.write(read_json)
  