import cv2
import numpy as np
framewidth = 640
frameheight = 480
minarea = 5000
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 100)
color = (0, 200, 0)
# path = 'C:\\Users\\Acer\\Pictures\\Elon_musk.jpg'
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
count = 2
# img = cv2.imread(path)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)
    for (x, y, w, h) in faces:
        area = w*h
        
        if area > minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 2), 2)
            cv2.putText(img, 'Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI',imgRoi)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Resources/scanned/Face_'+str(count)+'.jpg',imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
# for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow("Elon_musk",img)
# cv2.waitKey(0)