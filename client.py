import cv2
import socket
import time
import serial
from custom_socket import CustomSocket
import json
import os
from gtts import gTTS

line1 = 'The lights will turn red in'
line2 = 'three'
line3 = 'two'
line4 = 'one'
line1_mp3 = gTTS(text=line1, lang='en', slow=False)
line1_mp3.save("line1.mp3")
line2_mp3 = gTTS(text=line2, lang='en', slow=False)
line2_mp3.save("line2.mp3")
line3_mp3 = gTTS(text=line3, lang='en', slow=False)
line3_mp3.save("line3.mp3")
line4_mp3 = gTTS(text=line4, lang='en', slow=False)
line4_mp3.save("line4.mp3")
#arduino = serial.Serial('/dev/ttyACM0', 115200, timeout = 10)
time.sleep(1)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# host = "172.20.10.10"
host = "localhost"
port = 10101
c = CustomSocket(host, port)
c.clientConnect()
x = 0
delaynum = 0

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
        c.sock.send(delaystr)
        delaystr = delaystr.encode()
        #arduino.write(delaystr)
        i = delaynum
        while i >= 0:
            time.sleep(1)
            if(i == 5):
                os.system("open line1.mp3")
            elif(i==3):
                os.system("open line2.mp3")
            elif(i==2):
                os.system("open line3.mp3")
            elif(i==1):
                os.system("open line4.mp3")
            i -= 1;
        x = 0
        cap.release()
        cap = cv2.VideoCapture(0)
        cap.set(3,1280)
        cap.set(4,720)

    if cv2.waitKey(1) == ord('q'):
        cap.release()

cv2.destroyAllWindows()