import random
import time
import pyautogui
import pydirectinput
import subprocess
import pyttsx3
import os
import cv2
from tkinter import messagebox

tts = pyttsx3.init()

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

notes = ["subscribe", "PEAK", "PEAK is fun", "I probably just died", "I just died", "@MysticFlameYT", "@RealTeeBe", "Thanks to @RealTeeBe for making this code", "Oh No!", "like the video", "gamers", "gaming", "shameless plug (@RealTeeBe)"]
voicemessages = ["subscribe", "like", "make sure to check out @RealTeeBe", "when you shamelessly plug your channel in a video with a text to speech voice, @RealTeeBe", "you're probably gonna die", "hi mystic", "hi", "hello", "*vine boom*", "im always watching by the ways", "peak video", "l video", "peak", "peak is fun", "when is portal video number 14 coming out", "you make too many portal videos", "github.com/darkcookiesf", "w video", "im just here to annoy you", "lol", "haha", "why", "i am rapidly approaching your exact location", "tea be was gonna add a random webcam pop-up but deemed it too mean", "this is not a virus i swear", os.getlogin(), "did you ever have an annoying sibling as a kid", "fear me", "whats 1+1", "what", "what if i said your home location right now? i wont by the ways, winky face"]

def window():
    givenNote = random.choice(notes)
    writtenNote = pyautogui.prompt(givenNote) #writtenNote is input from prompt
    if givenNote != writtenNote: #incorrect responses go to windows2 and start looping
        window2(givenNote)

def window2(givenNote): #incorrect responses won't change from random choice
    writtenNote = pyautogui.prompt(givenNote)
    if givenNote != writtenNote:
        window2(givenNote)


input("Hello Mystic. Yes, this is a direct message to you. Click Enter to proceed.")
input("I have seen that in most of your videos, you have rules.")
input("So, before you start this script, how about *I* make the rules.")
input("Ok, here they are.")
print("")
input("Rule 1. NO closing this script until the challenge is over, if you close it even once, you must either restart, or admit being a cheater. (If the script closes due to an error, it is not your fault, reopen the script and continue the challenge.)")
input("Rule 2. Any method of climbing is legal.")
input("Rule 3. You cannot close any pop-ups, you must either use the buttons or answer box provided.")
input("Rule 4. (Try) to have fun! (After you click enter, this script will start)")


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

    doNoClimb = random.randint(0, 1)

    if doNoClimb == 1:
        for i in range(random.randint(26, 260)):
            pydirectinput.click("left")
            time.sleep(0.2)

    doRagdoll = random.randint(0,1)

    if doRagdoll == 1:
        pydirectinput.keyDown("r")
        pydirectinput.move(0, 100)
        pydirectinput.keyUp("r")

    doMoveKeys = random.randint(0, 1)

    if doMoveKeys == 1:
        num = random.randint(1,4)

        match num:
            case 1:
                pydirectinput.keyDown("w")
                time.sleep(random.randint(0,5))
                pydirectinput.keyUp("w")
            case 2:
                pydirectinput.keyDown("a")
                time.sleep(random.randint(0,5))
                pydirectinput.keyUp("a")
            case 3:
                pydirectinput.keyDown("s")
                time.sleep(random.randint(0,5))
                pydirectinput.keyUp("s")
            case 4:
                pydirectinput.keyDown("d")
                time.sleep(random.randint(0,5))
                pydirectinput.keyUp("d")

    doPopup = random.randint(0, 1)

    if doPopup == 1:
        givenNote = random.choice(notes)
        PopupDisplay = random.randint(1, 4)
        match PopupDisplay:
            case 1:
                messagebox.showinfo("Annoying Popup", givenNote)
            case 2:
                messagebox.showerror("Annoying Popup", givenNote)
            case 3:
                messagebox.showwarning("Annoying Popup", givenNote)
            case 4:
                messagebox.askquestion("Annoying Popup", givenNote)

    doPrompt = random.randint(0,1)

    if doPrompt == 1:
        window()

    doExit = random.randint(0,1)

    if doExit == 1:
        pydirectinput.press("esc")

    doNotepad = random.randint(0,1)

    if doNotepad == 1:
        subprocess.run(["notepad.exe"])

    doPaint = random.randint(0, 1)

    if doPaint == 1:
        subprocess.run(["mspaint.exe"])

    doCommandPrompt = random.randint(0, 1)

    if doCommandPrompt == 1:
        subprocess.run(["cmd.exe"])

    doMediaPlayer = random.randint(0, 1)

    if doMediaPlayer == 1:
        subprocess.run(["dvdplay.exe"])

    doTaskManager = random.randint(0, 1)

    if doTaskManager == 1:
        subprocess.run(["LaunchTM.exe"])

    doOSK = random.randint(0, 1)

    if doOSK == 1:
        subprocess.run(["osk.exe"])

    doSnippingTool = random.randint(0, 1)

    if doSnippingTool == 1:
        subprocess.run(["SnippingTool.exe"])

    doWinver = random.randint(0, 1)

    if doWinver == 1:
        subprocess.run(["winver.exe"])

    doWordPad = random.randint(0, 1)

    if doWordPad == 1:
        subprocess.run(["write.exe"])

    doTalk = random.randint(0,1)

    if doTalk == 1:
        tts.say(random.choice(voicemessages))

    if doMove and doScroll and doClick and doDrag and doDrop and doRun and doThrow and doNoClimb and doMoveKeys and doPopup and doPrompt and doExit and doNotepad and doPaint and doCommandPrompt and doMediaPlayer and doTaskManager and doOSK and doSnippingTool and doWinver and doWordPad and doTalk == 0:
        print("nothing happened, skipping iteration")
        time.sleep(0)
    else:
        print("round completed")
        time.sleep(random.randint(0, 60))
