import random
import time

import pyautogui

pyautogui.FAILSAFE = False

while True:
    doMove = random.randint(0, 1)

    if doMove == 1:
        pyautogui.moveTo(random.randint(0, 1920), random.randint(0, 1080), random.randint(0, 2))

    doDrag = random.randint(0, 1)

    if doDrag == 1:
        pyautogui.dragTo(random.randint(0, 1920), random.randint(0, 1080), random.randint(0, 2))

    doClick = random.randint(0, 1)

    if doClick == 1:
        lMOrR = random.randint(0, 2)
        clickAmount = random.randint(0, 2)

        if lMOrR == 0:
            pyautogui.leftClick()
            if clickAmount == 1:
                pyautogui.doubleClick()
            elif clickAmount == 2:
                pyautogui.tripleClick()
            else:
                time.sleep(0)
        elif lMOrR == 1:
            pyautogui.middleClick()
        else:
            pyautogui.rightClick()

    doScroll = random.randint(0, 1)

    if doScroll == 1:
        pyautogui.scroll(0)

    if doMove and doScroll and doClick and doDrag == 0:
        print("nothing happened, skipping iteration")
        time.sleep(0)
    else:
        print("round completed")
        time.sleep(random.randint(0, 60))
