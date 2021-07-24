import matplotlib.pyplot as plt
from PIL import Image

p = "./images/dmm.png"

if __name__=='__main__':

  im = Image.open(p)
  plt.imshow(im)