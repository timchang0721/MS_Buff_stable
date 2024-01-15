import pyautogui
import pydirectinput
import pyperclip
import time
import re
from datetime import datetime
from PIL import Image , ImageEnhance, ImageOps
import pytesseract
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

def checkmember():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(397,160, 41, 95))
    im.save('people.png')
    img = Image.open("people.png")
    text = pytesseract.image_to_string(img, lang='eng')
    text.split('\n')
    print("現在隊員數為 "+str((len(text.split('\n')))))
    if len(text.split('\n'))>=5:
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
            word("輸入的金額不對 價格改為1000W一次")
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
    print(ans)
    return int(ans)
    
def checktradecomplete():
    global account
    new_account = checkaccount()
    if new_account!=account:
        account = new_account
        return True
    return False
   
def techcooldown(time,cd):
    if time<=cd:
        #if time%45==1:
        #    key('3')
        if time%32==31:
             word("冷卻結束  1000W一次     密我:a     記得退組    記得退組")  
        if time%31==23:
            word("冷卻剩餘10秒... 請稍等  1000W一次   記得退組    記得退組")  
        if time%31==15:
            word("冷卻剩餘20秒... 請稍等  1000W一次   記得退組    記得退組") 
        if time%31==7:
            word("冷卻剩餘30秒... 請稍等  1000W一次   記得退組    記得退組")

 
        #elif time%10==0:
            #key('6')

          
def reset():
    global resettimes
    resettimes+=1
    if resettimes%2 == 0:
        word("111111111111111111")
    if resettimes%2 == 1:
        word("11111111111111111") 

if __name__ == '__main__':
    money = 10000000
    cd = 31
    waittime = cd
    checkmoneyflag= False
    errortimes = 0
    resettimes = 0
    secussfulltimes = 0
    account= checkaccount()
    #reset()
    time.sleep(5)
    while 1:
        loopflag = True
        techcooldown(waittime,cd)
        #if secussfulltimes ==2:
            #key('9')
            #secussfulltimes=0
        if waittime > cd :
            if waittime % 20 ==1:
                word("buff 1000W一次 密我:a 站我的左邊   記得退組    記得退組")
            if waittime % 20 ==6:
                word("buff 1000W一次 密我:a 站我的左邊   記得退組    記得退組.")
            if waittime % 20 ==11:
                word("buff 1000W一次 密我:a 站我的左邊   記得退組    記得退組")
            if waittime % 20 ==16:
                word("buff 1000W一次 密我:a 站我的左邊   記得退組    記得退組.")   
            getID()
            id = pyperclip.paste()
            print(id)          
            if  id != "沒錢又沒裝" and id != "buff機3號" :
                key('5') 
                #now = datetime.now()
                #print(f"目前時間: {now.strftime('%Y-%m-%d %H:%M:%S')}")
                copyword("/交易",id)#跟玩家交易
                for k in range(0,20):
                    time.sleep(0.5)
                    if k == 0:
                        firsttimein= True
                    if loopflag == False:
                        break
                    #if checkintrade():
                        #if firsttimein == True : 
                            #word("放一次buff為200W")
                            #word ("交易會在10秒鐘後關閉.....")
                            #firsttimein = False           
                    if k == 19:
                        pydirectinput.click(518,241) #交易逾時取消交易
                        pydirectinput.click(734,411)#按下交易終止確認
                        print ("交易取消")
                        word ("價格改為1000W一次")
                        #reset()#清掉h密語的欄位
                        errortimes = 0
                        break
                    if checktradecomplete() and checkmoneyflag == True:#確認玩家是否按下交易
                        errortimes = 0
                        time.sleep(0.5)
                        pyautogui.hotkey('enter')
                        for j in range(0,5):#給使用者三次組隊的機會
                            
                            if j == 4 or loopflag == False:
                                loopflag = False
                                #reset()
                                #reset()
                                word("冷卻剩餘40秒... 請稍等 1000W一次 請先退組")
                                pydirectinput.keyDown('left')
                                time.sleep(3)
                                pydirectinput.keyUp('left')
                                pydirectinput.keyDown('right')
                                time.sleep(2)
                                pydirectinput.keyUp('right')
                                break
                            if j >=1:
                                pydirectinput.click(734,411)
                                word("請退出組隊 請退出組隊 沒退出不退錢")    
                            time.sleep(1)
                            pydirectinput.click(734,411)
                            copyword("/組隊邀請",id)
                            time.sleep(0.5)
                            pyautogui.hotkey('enter')
                            for i in range(0,3):#每次組隊經驗為3秒鐘
                                time.sleep(1)
                                if checkmember() :#確認已經入隊
                                    #time.sleep(1)
                                    pydirectinput.click(734,411)
                                    #future = datetime.now()
                                    #print(f"50秒後的時間: {future.strftime('%Y-%m-%d %H:%M:%S')}")
                                    #difference = future - now
                                    #print (difference)    
                                    leopard()
                                    time.sleep(6)
                                    waittime = 0
                                    copyword("/組隊踢人",id)
                                   # secussfulltimes+=1
                                    #time.sleep(2)

                                    loopflag = False
                                    break 
                    if checkmoney(money) :#確認玩家輸入的金額是否正確
                        pydirectinput.click(520,218)#按下交易
                        pydirectinput.click(688,411)
                        print("金額確認無誤")
                        checkmoneyflag = True

                                            
        time.sleep(1)
        waittime+=1

            
       
   
