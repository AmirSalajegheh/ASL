import cv2
from ultralytics import YOLO


model = YOLO("Data/best.pt")


cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("asl_detection.mp4", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    results = model.track(source=frame, persist=True, show=False)

    
    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cls_id = int(box.cls[0])
                label = model.names[cls_id]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("ASL Detection", frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()