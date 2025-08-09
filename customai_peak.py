import random
import time
import pyautogui
import pydirectinput

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

while True:
    doMove = random.randint(0, 1)

    if doMove == 1:
        pydirectinput.moveTo(random.randint(0, 1920), random.randint(0, 1080), random.randint(0, 2))

    doDrag = random.randint(0, 1)

    if doDrag == 1:
        pyautogui.dragTo(random.randint(0, 1920), random.randint(0, 1080), random.randint(0, 2))

    doClick = random.randint(0, 1)

    if doClick == 1:
        lMOrR = random.randint(0, 2)
        clickAmount = random.randint(0, 2)

        if lMOrR == 0:
            pydirectinput.leftClick()
            if clickAmount == 1:
                pydirectinput.doubleClick()
            elif clickAmount == 2:
                pydirectinput.tripleClick()
            else:
                time.sleep(0)
        elif lMOrR == 1:
            pydirectinput.middleClick()
        else:
            pydirectinput.rightClick()

    doScroll = random.randint(0, 1)

    if doScroll == 1:
        pyautogui.scroll(0)

    doRun = random.randint(0, 1)

    if doRun == 1:
        pydirectinput.keyDown("shift")
        time.sleep(random.randint(1, 30))
        pydirectinput.keyUp("shift")

    doDrop = random.randint(0,1)

    if doDrop == 1:
        pydirectinput.press(str(random.randint(1,4)))
        pydirectinput.press("q")

    doThrow = random.randint(0,1)

    if doThrow == 1:
        pydirectinput.press(str(random.randint(1,4)))
        pydirectinput.keyDown("q")
        time.sleep(random.randint(1,3))
        pydirectinput.keyUp("q")

    if doMove and doScroll and doClick and doDrag == 0:
        print("nothing happened, skipping iteration")
        time.sleep(0)
    else:
        print("round completed")
        time.sleep(random.randint(0, 60))
