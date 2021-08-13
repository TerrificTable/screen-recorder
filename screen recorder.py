import cv2 as cv
import numpy as np
import pyautogui
import keyboard # if you dont use the while loop or deside to remove the "hotkey" delet this import too

screen = (1920, 1080) # Change the values to change screen/recording size
format = cv.VideoWriter_fourcc(*"MPG4") # Change the String to get another Video Format
output = cv.VideoWriter("output.mp4", format, 30, screen) # Change the String to whatever you want the output file to be nemed just keep the ".mp4" there, Change the "30" to change the framerate

# Use the "for loop" below if you want
# change the the second integer stands for the seconds, use this if you want to have a fixed video length
""" for i in range(30*5): """
while keyboard.is_pressed("q") != True: # Change the String to get another key to stop recording
    img = pyautogui.screenshot() # put "region=(startX, startY, endX, endY)" if you only want to record a fixed region of your screen
    video = np.array(img)
    video = cv.cvtColor(video, cv.COLOR_BGR2RGB) # Change the cv.COLOR_ to get other Color scemes
    output.write(video)

output.release()
