import pyautogui as ag
import threading as t
import time
import os
import sys
from pynput import keyboard

class RepeatTimer(t.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def check_chicken():
    btn = ag.locateOnScreen('./click/image.png')
    if btn is not None:
        a,b = ag.center(btn)
        ag.moveTo(a,b)
        ag.mouseDown()

    chicken = ag.locateOnScreen('./click/image2.png')
    if chicken is not None:
        ag.mouseUp()
    
    chicken = ag.locateOnScreen('./click/image3.png')
    if chicken is not None:
        ag.mouseDown()

b = True
def check_garbage():
    pos = [(1242,473),(790,450),(802,463),(808,481),(805,493),(796,507),(783,512),(766,512),(751,512),(742,503),(737,492),(736,482),(735,472),(739,465),(745,457),(751,456),(760,450),(769,448),(772,448)]

    x, y = 1018,450
    # ag.moveTo(x, y)
    # ag.mouseDown()
    # ag.moveTo(pos[0][0], pos[0][1])
    while True:
        if b:
            ag.click()
            # for i in range(len(pos)):
            #     ag.moveTo(pos[i][0], pos[i][1], 0)
        else:
            time.sleep(1)

def locate_image(image):
    return ag.locateOnScreen(image)

# th = [t.Thread(target=check_garbage, daemon=True) for a in range(5)]
# for a in th:
#     a.start()
def start():
    global b
    b = True
    
def stop():
    global b
    b = False

def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    
    if k == 'a':
        start()
    elif k == 'q':
        sys.exit()
    else:
        stop()
        


# rep = RepeatTimer(5, check_chicken)
# rep.start()

# while True:
#     time.sleep(1)

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    check_garbage()
     #ag.mouseInfo()