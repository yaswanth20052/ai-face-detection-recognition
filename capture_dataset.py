import cv2
import os

name = input("Enter your name: ")

path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        cv2.imwrite(f"{path}/{count}.jpg", face)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Capturing Dataset", frame)

    if cv2.waitKey(1)==13 or count>=50:
        break

cap.release()
cv2.destroyAllWindows()