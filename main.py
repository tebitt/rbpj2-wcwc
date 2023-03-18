from custom_socket import CustomSocket
from ultralytics import YOLO
import socket
import numpy as np
import json
import traceback
from gtts import gTTS
import os
import time

model = YOLO("wcc_best_3.pt")
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

def main():
   # HOST = "172.20.10.10"
    HOST = 'localhost'
    PORT = 10101

    server = CustomSocket(HOST, PORT)
    server.startServer()
    
    while True:
      
      conn, addr = server.sock.accept()
      print("Client connected from", addr)
      
      while True:
        try:
            data = server.recvMsg(conn)
            frame = np.frombuffer(data, dtype=np.uint8).reshape(720, 1280, 3)
            res = model.predict(source=frame, conf=0.5, show = True)[0]
            Detected = []
            if res.boxes:
                Detected = []
                for r in res.boxes:
                    for c in res.boxes.cls:
                        print(model.names[int(c)])
                        Detected.append(model.names[int(c)])
                        break

            print(Detected)
            server.sendMsg(conn, json.dumps(Detected))

        except Exception as e:
                traceback.print_exc()
                print(e)
                print("Connection Closed")
                del res
                break
            
if __name__ == '__main__': 
  main()