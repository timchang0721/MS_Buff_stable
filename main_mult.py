import pyautogui
import pydirectinput
import pyperclip
import time
import re
from datetime import datetime
from PIL import Image , ImageEnhance, ImageOps
import pytesseract
import queue
def key(word):
    pydirectinput.keyDown(word)
    pydirectinput.keyUp(word)
def word(word):
    abc= word
    pyperclip.copy(abc)
    pyautogui.hotkey('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    abc=""

def copyword(instruction,id):
    a=instruction+" "+id
    print (a)
    pyperclip.copy(a)
    pyautogui.hotkey('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    a=""
def getID():
    key('h')
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('c')
    pydirectinput.keyUp('c')
    pydirectinput.keyUp('ctrl')
    key('esc')


def leopard():
    key('1')
    time.sleep(0.5)
    key('2')

def checkmember(num_beforemember):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(397,160, 41, 95))
    im.save('people.png')
    img = Image.open("people.png")
    text = pytesseract.image_to_string(img, lang='eng')
    text.split('\n')
    print("現在隊員數為 "+str((len(text.split('\n')))))
    if len(text.split('\n'))>num_beforemember+1:
        return True
    return False
def checkintrade(): #是否進入交易
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(434,298,84 , 19))
    #im = pyautogui.screenshot(region=(467,441,77 , 14))
    im.save('intrade.png')
    img = Image.open("intrade.png")
    # Convert the image to grayscale
    img = img.convert('L')
    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Increase contrast; you can adjust the factor as needed
    # Binarize the image
    img = ImageOps.invert(img)
    threshold = 100
    img = img.point(lambda p: p > threshold and 255)
    text = pytesseract.image_to_string(img, lang='eng+chi_tra')
    print("此交易腳色ID為"+text)
    if text!="":
        return True
    else:
        return False
     
def checkmoney(money):
    global errortimes
    global firsttimein 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(425,408,75 , 14))
    im.save('money.png')
    img = Image.open("money.png")
    text = pytesseract.image_to_string(img, lang='eng')
    text.split('\n')
    ans = text.split('\n')[0].replace(",","")
    ans = ans.split('\n')[0].replace(".","")
    ans = re.sub(r'\D', '', ans)
    print("玩家輸入的金額是"+ans)
    if ans =="":
        return False
    if ans.isdigit():
        if int(ans) == money :
            return True
        elif int(ans)!= money and errortimes ==0:
            word("輸入的金額不對")
            errortimes = 1
            return False

    return False
def checkaccount():
    global account
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(1150,380,81 ,16))
    im.save('account.png')
    img = Image.open("account.png")
    text = pytesseract.image_to_string(img, lang='eng')
    ans = re.sub(r'\D', '', text)
    print (ans)
    return int(ans)

def checktradecomplete():
    global account
    new_account = checkaccount()
    if new_account!=account:
        account = new_account
        return True
    return False
def reset(name):
    key('h')
    abc= name
    pyperclip.copy(abc)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    key('enter')
    abc= "/全"
    pyperclip.copy(abc)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    key('enter')
    key('enter')
def callperson(name):
    key('h')
    abc= name
    pyperclip.copy(abc)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    key('enter')
    abc= "1"
    pyperclip.copy(abc)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    key('enter')
    key('enter')
if __name__ == '__main__':
    money = 2000000
    cd = 55
    catname="殺區貓貓仔"
    doorname="殺區天門"
    resetname="快樂商人5號"
    checkmoneyflag= False
    resettimes = 0
    secussfulltimes = 0
    account= checkaccount()
    num_beforemember= 3
    wait_for_others= 3
    people_in_team = False
    tech_ready = True
    time_delta = 0
    people = []
    time.sleep(5)
    reset(resetname)
    now = datetime(2022,1,1) 
    while 1:
        loopflag = True
        time_delta = int ((datetime.now() - now).total_seconds())
        if time_delta >= cd :
            tech_ready = True
            if  time_delta % 10 == 1 :
                word("buff試營運  只要200W   需要密語我   站我我左邊   記得退組    記得退組")
            elif  time_delta % 10 ==  6:
                word("buff試營運  只要200W   需要密語我   站我我左邊   記得退組    記得退組.")   
        elif time_delta % 10 ==3 :
            word("冷卻剩餘"+str(cd-time_delta)+"秒......... 試營運200W   需要密語我      可先進組")   
        if tech_ready == True and people_in_team == True:    
            if  num_beforemember == 6 or wait_for_others <0 :
                callperson(catname)
                time.sleep(1)
                callperson(doorname)
                leopard()
                now = datetime.now() 
                time.sleep(3)
                while people:
                    copyword("/組隊踢人",people.pop())
                    time.sleep(0.5)
                reset(resetname)    
                word("冷卻剩餘50秒......... 試營運200W   需要密語我      可先進組")
                num_beforemember = 3
                people_in_team= False
                tech_ready = False
                pydirectinput.keyDown('left')
                time.sleep(3)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('right')
                time.sleep(2)
                pydirectinput.keyUp('right')
        if  people_in_team == True :
            wait_for_others -=1                  
        getID()
        id = pyperclip.paste()
        print(id)
        if id not in people :
            if id!= resetname and num_beforemember <6 :#確認人數在6人以下
                word("交易中....其他玩家請稍等")
                copyword("/交易",id)#跟玩家交易
                for k in range(0,20):
                    time.sleep(0.5)
                    if loopflag == False:
                        break      
                    if k == 19:
                        pydirectinput.click(518,241) #交易逾時取消交易
                        pydirectinput.click(734,411)#按下交易終止確認
                        print ("交易取消")
                        reset(resetname)
                        break
                    if checkmoney(money) :#確認玩家輸入的金額是否正確
                        pydirectinput.click(520,218)#按下交易
                        pydirectinput.click(688,411)#按下確認
                        print("金額確認無誤")
                        checkmoneyflag = True    
                    if checktradecomplete() and checkmoneyflag == True:#確認玩家是否按下交易
                        time.sleep(0.5)
                        pyautogui.hotkey('enter')
                        for j in range(0,5):#給使用者三次組隊的機會
                            if j >=2:
                                word("請加入組隊或退出原本的組隊")
                            if j == 4 or loopflag == False:
                                loopflag = False
                                reset(resetname)
                                break
                            time.sleep(1)
                            #pyautogui.hotkey('enter')
                            copyword("/組隊邀請",id)
                            time.sleep(0.5)
                            pyautogui.hotkey('enter')
                            word("組隊中....其他玩家請稍等")
                            for i in range(0,3):#每次組隊經驗為3秒鐘
                                time.sleep(1)
                                if checkmember(num_beforemember) :#確認已經入隊
                                    num_beforemember+=1
                                    pyautogui.hotkey('enter')
                                    time_delta = int ((datetime.now() - now).total_seconds())
                                    if time_delta >= cd :
                                        word("如果還有人要請在3秒內密我")  
                                    else:
                                        word("技能冷卻中 試營運200W   需要密語我     可先進組.")
                                    loopflag = False
                                    people_in_team = True
                                    people.append(id)
                                    wait_for_others = 2
                                    break                            
        time.sleep(1)        
    
   
