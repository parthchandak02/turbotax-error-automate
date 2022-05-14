import pyautogui
import time
import re

loadingImg = 'Images\\BLANK_COINBASE.png'
page1 = 'Images\\0_PAGE1.png'
page2 = 'Images\\0_PAGE2.png'
page3 = 'Images\\0_PAGE3.png'

fixImg = 'Images\\1_FIX.png'
otherImg = 'Images\\2_OTHER.png'
blankImg = 'Images\\3_BLANK.png'
variousImg = 'Images\\4_VARIOUS.png'
continueImg = 'Images\\5_CONTINUE.png'
noneImg = 'Images\\6_NONE.png'


defaultWaitTimeSecs = 15
pyautogui.FAILSAFE = True

def defaultLoc():
    pyautogui.moveTo(100, 150)

def wait(x):
    i = 1
    while i <= x:
        print("waiting... " + str(i) + " seconds")
        time.sleep(1)
        i+=1

def waitToLoad():
    defaultLoc()
    try:
        coinbase_x,coinbase_y=pyautogui.locateCenterOnScreen(loadingImg,grayscale=True,confidence=0.7)
        if coinbase_x > 0:
            try:
                page3_x,page3_y=pyautogui.locateCenterOnScreen(page3,grayscale=True,confidence=0.7)
                if page3_x > 0:
                    print("We are on page 3!")
                    return
            except:
                print("Loading...")
                wait(3)
                waitToLoad()
    except:
        return False


def clickFromLocation(ImageLocation):
    try:
        x,y=pyautogui.locateCenterOnScreen(ImageLocation,grayscale=True,confidence=0.7)
        pyautogui.click(x,y)
        print("clicked on image from " + str(ImageLocation))
    except:
        print("SKIPPED! cound't find image from " + str(ImageLocation))
        return

def scroll(Pixels):
    pyautogui.scroll(Pixels)
    print("scrolled down "+ str(Pixels) +" pixels")


def sequence():
    defaultLoc()
    # page 1
    clickFromLocation(fixImg)
    wait(2)
    waitToLoad()
    # page 2
    scroll(-500)
    clickFromLocation(otherImg)
    wait(2)
    clickFromLocation(blankImg)
    wait(2)
    clickFromLocation(variousImg)
    scroll(-1500)
    clickFromLocation(continueImg)
    wait(2)
    waitToLoad()
    # page 3
    clickFromLocation(noneImg)
    wait(2)
    clickFromLocation(continueImg)
    waitToLoad()

counter = 0
while counter < 4:
    counter+=1
    print("Error #" + str(counter))
    sequence()
    print("--------------------------------------------------")