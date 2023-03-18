from custom_socket import CustomSocket
from ultralytics import YOLO
import socket
import numpy as np
import json
import traceback

model = YOLO("wcc_best_3.pt")

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