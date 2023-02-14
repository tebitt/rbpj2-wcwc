import cv2
import time
from ultralytics import YOLO

model = YOLO("best.pt")

current_time = 0
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        ("Camera failure")
        continue
        
    cv2.putText(frame, str(round(1 / (time.time() - current_time), 1)) + ' fps', (25, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    current_time = time.time()
    res = model.predict(source=frame, conf=0.7, show = True)[0]
    Detected = []
    if res.boxes:
        for r in res:
            for c in res.boxes.cls:
                Detected.append(model.names[int(c)])



    # cv2.imshow( "Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        cap.release()
    time.sleep(4)

cv2.destroyAllWindows()