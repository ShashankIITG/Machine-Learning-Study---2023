import cv2

cap = cv2.VideoCapture(1)
while True:
      
    a, f = cap.read()

    if a == False:
        continue

    cv2.imshow("video frame", f)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()