import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
skip = 0

face_data = []
file_path = './data/'
file_name = input("Enter your name : ")

while True:
    ret,frame = cap.read()

    if ret == False:
        print("error in capturing frame || retrying")
        continue

    # 1.3 is scaling parameter and 5 is number of neighbour
    face_locations = face_cascade.detectMultiScale(frame, 1.3, 5)
    face_locations = sorted(face_locations, key = lambda f:f[2]*f[3], reverse=True)
    
    #print(face_locations)

    for face_location in face_locations:
        x, y, w, h = face_location
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        offset = 10
        face = frame[y-offset : y+h+offset, x-offset : x+w+offset]
        face = cv2.resize(face, (100, 100))

        cv2.imshow("cropped face", face)

        skip += 1
        if skip%5 == 0:
            face_data.append(face)
            print(len(face_data))

    cv2.imshow("video frames", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

face_data = np.array(face_data)
print(face_data.shape)
face_data = face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)

np.save(file_path + file_name + '.npy', face_data)
print("file data successfully saved at " + file_path + file_name + '.npy')

cap.release()
cv2.destroyAllWindows()