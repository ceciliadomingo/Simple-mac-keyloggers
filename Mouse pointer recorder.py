from pynput import mouse
import datetime

#OUTPUT EXAMPLE
#Mouse: Move(x=1105, y=634) Time: 2023-04-20 16:33:43.866504
#Mouse: Click(x=492, y=278, button=Button.left, pressed=True) Time: 2023-04-20 16:33:44.730328


#DEFINING OUTPUT FORMAT
def on_move(x, y):
    with open("Mouse.txt", "a") as f:
        f.write("Mouse: Move%s Time: %s \n" %((x, y),datetime.datetime.now()))

def on_click(x, y, button, pressed):
    with open("Mouse.txt", "a") as f:
        if pressed:
            f.write("Mouse: Click%s Time: %s \n" %((x, y,button,pressed),datetime.datetime.now()))
        else:
            f.write("Mouse: Released%s Time: %s \n" %((x,y,button,pressed),datetime.datetime.now()))

#MOUSE POINTER RECORDER
def start_recording():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click) as listener:
        listener.join()

#Call function to start recording
start_recording()
