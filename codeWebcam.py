import cv2
import pytesseract
import numpy as np 
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 170)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("CANNOT OPEN")

cntr = 0
while True:
    ret,frame = cap.read()
    cntr = cntr + 1
    if((cntr%1)==0):
        imgH, imgW,_ = frame.shape
        x1,y1,h1,w1 = 0,0,imgH,imgW
        imgchar = pytesseract.image_to_string(frame, lang='eng')
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes=boxes.split(' ')
            x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame, (x, imgH-y),(w,imgH-h),(0,0,255),3)

        #cv2.rectangle(frame, (x1, x1),(x1+w1,y1+h1),(0,0,), -1)
        cv2.putText(frame, imgchar, (x1 + int(w1/50), y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.imshow('text detection',frame)
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break
print(imgchar)
cap.release()