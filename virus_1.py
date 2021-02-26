import pyautogui
# import PIL   #pillow
from PIL import Image,ImageGrab,ImageOps
from numpy import asarray


while True :
    img=ImageGrab.grab().convert('L')
    imgdata=img.load()
    img.show()