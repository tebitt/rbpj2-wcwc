import cv2
import socket
import time
import serial
from custom_socket import CustomSocket
import os
import json
from gtts import gTTS

#arduino = serial.Serial('/dev/ttyACM0', 115200, timeout = 10)
time.sleep(1)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

host = "localhost"
port = 10101
c = CustomSocket(host, port)
c.clientConnect()
x = 0
delaynum = 0
line1 = 'The lights will turn red in three'
line2 = 'two'
line3 = 'one'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        ("Camera failure")
        continue
    
    msg = c.req(frame)
    if msg != []:
        x += 1
        # for i in msg:
        #     Dict[i] += 1
        Dict = dict()
        for i in msg:
            Dict[i] = Dict.get(i, 0) + 1
            print(Dict)
        DictKey = list(Dict.keys())


        #### Average time people use for walking is about 10 - 20 seconds ####
    else: x = 0
    print("Condition check x = "+ str(x))
    if(x == 5) :
        print("Count = 5")
        DictKey = list(Dict.keys())
        delay = 10
        for k in DictKey :
           if(k == "person") :
              #  if(dict[k] > 3) :
              #      delay += dict[k]*0.2
              #  else : pass
               delay += Dict[k]*0.2
           elif(k == "wheel_chair") :
               delay += Dict[k]*3
           elif(k == "cane") :
               delay += Dict[k]*1.5
        delaynum = round(delay)
        delaystr = str(delaynum)
        delaystr = delaystr.encode()
        #arduino.write(delaystr)
        x = 0
        i = delaynum
        while i >= 0:
            time.sleep(1)
            if(i == 6):
                os.system("open line1.mp3")
                time.sleep(1)
            elif(i==1):
                os.system("open line2.mp3")
            elif(i==0):
                os.system("open line3.mp3")
            i -= 1;
        time.sleep(delaynum)
        cap.release()
        cap = cv2.VideoCapture(0)
        cap.set(3,1280)
        cap.set(4,720)

    if cv2.waitKey(1) == ord('q'):
        cap.release()

cv2.destroyAllWindows()
