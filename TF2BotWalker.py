# CODE

import keyboard
import pyautogui
import time
import random
specialMovment = 0
specialDirection = 0
waitTime = 0
turnDirection = 0
turnSpeed = 0
print('program starts in 10 seconds')
time.sleep(10)
pyautogui.center
while True:
    if keyboard.read_key == 'p':
        quit
    else:
        specialMovment = random.randint(1, 5)
        if specialMovment == 1:
            specialDirection = random.randint(1, 3)
            if specialDirection == 1:
                waitTime = random.randint(10, 30)
                for i in range(1, waitTime):
                    pyautogui.typewrite('s')
                    print('backwards')
            else:
                if specialDirection == 2:
                    waitTime = random.randint(10, 30)
                    for i in range(1, waitTime):
                        pyautogui.typewrite('a')
                        print('left')
                else:
                    waitTime = random.randint(10, 30)
                    for i in range(1, waitTime):
                        pyautogui.typewrite('d')
                        print('right')
        else:
            waitTime = random.randint(10, 30)
            for i in range(1, waitTime):
                pyautogui.typewrite('w')
                print('forward')
        turnDirection = random.randint(-500, 500)
        turnSpeed = random.uniform(0.5, 1.5)
        pyautogui.moveRel(turnDirection, 0, duration=turnSpeed)

# TESTING SECTION

