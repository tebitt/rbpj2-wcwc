from custom_socket import CustomSocket
from ultralytics import YOLO
import socket
import numpy as np
import json
import traceback

model = YOLO("best.pt")

def main():
    HOST = socket.gethostname()
    PORT = 10101

    server = CustomSocket(HOST, PORT)
    server.startServer()
    
    while True:
      
      conn, addr = server.sock.accept()
      print("Client connected from", addr)
      
      while True:
        try:
            detected = []

            data = server.recvMsg(conn)
            frame = np.frombuffer(data, dtype=np.uint8).reshape(720, 1280, 3)
            res = model.predict(source=frame, conf=0.7, show = True)[0]
            Detected = []
            if res.boxes:
                for r in res:
                    for c in res.boxes.cls:
                        Detected.append(model.names[int(c)])

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