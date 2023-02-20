import cv2
import socket
import time
from custom_socket import CustomSocket
from street_timer import Street_Timer

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
        # Dict = {"person": 0, "wheel_chair": 0, "cane": 0 }
        # for i in msg:
        #     Dict[i] += 1
        Dict = dict()
        for i in msg:
            Dict[i] = Dict.get(i, 0) + 1
            print(Dict)
        #### Average time people use for walking is about 10 - 20 seconds ####
        # delay = Street_Timer(Dict["person"], Dict["wheel_chair"], Dict["cane"]).get_delay()
        # Street_Timer.lights_control(delay)
        # time.sleep(delay)
        
    

    # cv2.imshow( "Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        cap.release()
   # time.sleep(4)

cv2.destroyAllWindows()