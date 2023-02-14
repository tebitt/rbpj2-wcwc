import cv2
import socket
import time
from custom_socket import CustomSocket

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

host = "172.20.10.10"
port = 10101
c = CustomSocket(host, port)
c.clientConnect()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        ("Camera failure")
        continue
    
    msg = c.req(frame)
    if msg != []:
      print(msg)

    # cv2.imshow( "Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        cap.release()
    time.sleep(4)

cv2.destroyAllWindows()