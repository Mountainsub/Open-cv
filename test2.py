import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)

while True:
    succss, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
