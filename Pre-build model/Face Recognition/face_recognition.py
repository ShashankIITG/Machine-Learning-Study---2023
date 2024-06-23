from itertools import count
import cv2
import os
import numpy as np

# initalize camera
cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#### knn ####
def e_dist(x1, x2):
    return np.sqrt( sum( (x1 - x2)**2 ) )

def knn(train_X, train_Y, queryPoint, k = 7):
    dist = []
    points = train_X.shape[0]

    for i in range(points):
        # print(type(queryPoint), " ", type(train_X[i]))
        t_dist = e_dist(queryPoint, train_X[i])
        dist.append([t_dist, train_Y[i]])

    dist = sorted(dist)
    dist = dist[:k]

    dist = np.array(dist)
    freq = np.unique(dist[:, 1], return_counts = True)

    index = freq[1].argmax()
    pred = freq[0][index]

    return pred

#### face data preparation ####
dataset_path = './data/'
face_data = []
labels = []
names = {}
label_id = 0

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        ## load and read face pixels np array
        face_npy = np.load(dataset_path+fx)
        face_data.append(face_npy)
        print("loaded ", fx)

        ## create labels for each face data
        ids = label_id * np.ones((face_npy.shape[0]), )
        labels.append(ids)

        ## create names and labels mapping
        names[label_id] = fx[:4]

        ## increase label_id 
        label_id += 1

## face_data and labels have list of arrays one each for dataset npy file.
## concatenate arrays
face_dataset = np.concatenate(face_data, axis = 0)
labels_dataset = np.concatenate(labels, axis = 0)

print(face_dataset.shape)
print(labels_dataset.shape)

#### testing and classify face ####
while True:
    ret, frame = cap.read()

    if ret == False:
        print("retrying || ")
        continue

    faces_corr = face_cascade.detectMultiScale(frame, 1.3, 5)

    for face_corr in faces_corr:
        x, y, w, h = face_corr

        offset = 10
        face = frame[y-offset : y+h+offset, x-offset : x+h+offset]
        face = cv2.resize(face, (100, 100))

        ## predicted label (output)
        out = knn(face_dataset, labels_dataset, face.flatten())

        ## display predicted name on the window
        name = names[int(out)]
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA )
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)

    ## close window with q press
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
