import pyautogui
import pydirectinput
import pyperclip
import time
from PIL import Image 
import pytesseract
def key(word):
    pydirectinput.keyDown(word)
    pydirectinput.keyUp(word)
def cat():
    key('1')
    key('up')
    key('2')
    time.sleep(2.5)
    key('1')
    key('down')
    time.sleep(0.5)
    key('2')

def door():
    key('1')
    time.sleep(0.5)
    key('2')
    time.sleep(2)
    pydirectinput.keyDown('left')
    time.sleep(3)
    pydirectinput.keyUp('left')
    pydirectinput.keyDown('right')
    time.sleep(1)
    pydirectinput.keyUp('right')

def leopard():
    key('1')
    key('2')
  
def checkmember():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(397,160, 41, 95))
    im.save('member.png')
    img = Image.open("member.png")
    text = pytesseract.image_to_string(img, lang='eng')
    print(text.split('\n'))
    print(len(text.split('\n')))
    if len(text.split('\n'))==5:
        return True
    return False 
def checkreset():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(590,541, 100, 60))
    im.save('reset.png')
    img = Image.open("reset.png")
    text = pytesseract.image_to_string(img, lang='eng')
    print(text.split('\n'))
    print(len(text.split('\n')))
    if len(text.split('\n'))==4:
        return True
    return False 

if __name__ == '__main__':
    time.sleep(2)
    count = 0
    number = 0
    door()
    while True:
        while True :
            time.sleep(0.5)
            if checkmember()and number>20:
                door()
                number = 0
                break
            number+=1    
        #time.sleep(58)