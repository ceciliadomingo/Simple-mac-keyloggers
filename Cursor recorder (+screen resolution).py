import pyautogui
import datetime
import time

#SET DEFAULT VALUE FOR RECORDING
recording = True

#SCREEN RESOLUTION
screen_resolution = print(pyautogui.size(),file=open("screen_resolution-b.txt","w+"))

#CURSOR RECORDER
def start_recording():
    while recording == True:
        #RECORDING CURSOR
        print("Cursor: %s Time: %s" %(pyautogui.position(), datetime.datetime.now()),file=open("cursor_position-b.txt",'a+'))
        #Make the function wait for 0.25 seconds to reduce output granularity
        time.sleep(0.25)

#Call function to start recording
start_recording() 
