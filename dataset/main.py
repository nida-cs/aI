import cv2
import face recognition
import numpy as numpy 
import os
from datetime import datetime
import cvs 
path= 'dataset'
image= []
classnames= []

for file in os.listdir(path)
   img = cv2.imread(f'{path}'/{file})
    img.append(img)
    classnames.append(os.path.splitext(file)[0])
     print("student images loaded",classnames)

     def findEncodings(images):
        encodlist = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)


        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            markAttendance(name)
            
            # Draw box and name on screen

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
