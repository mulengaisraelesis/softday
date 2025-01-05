
'''
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # capture frame by frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# when everything done, release the capture
cap.release()
cv.destroyAllWindowsa'''

# Load a sample picture and learn how to recognize it.
import face_recognition
import cv2
import numpy as np

# Load the training image and get the encodings
img1 = face_recognition.load_image_file("training_picture/isra_train.jpeg")
img1_encoding = face_recognition.face_encodings(img1)

if len(img1_encoding) == 0:
    print("No faces found in the training image.")
    exit()
else:
    img1_encoding = img1_encoding[0]

# Load the test image and get the encodings
img2 = face_recognition.load_image_file("test_picture/isra_test.jpeg")
img2_encoding = face_recognition.face_encodings(img2)

if len(img2_encoding) == 0:
    print("No faces found in the test image.")
    exit()
else:
    img2_encoding = img2_encoding[0]

# Compare faces
results = face_recognition.compare_faces([img1_encoding], img2_encoding)
print("Are the faces matching? ", results)
