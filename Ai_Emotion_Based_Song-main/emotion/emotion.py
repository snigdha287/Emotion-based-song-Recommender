import numpy as np
import cv2
import os
# import tensorflow as tf
# from tensorflow import keras
import pyautogui as pg
# path = "./haarcascades/haarcascade_frontalface_alt2.xml"
# face = cv2.CascadeClassifier(path)
#
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('filename.mp4')
from time import perf_counter_ns



def fun(path,name_path,face,cap):
    i = 0
    while True:
        _,img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # n, m = map(int, input().split())
        # t1_start = perf_counter_ns()

        for(x,y,w,h) in faces:
            if (x!=0 or y!=0):
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                img1 = img[y:y+h,x:x+w]  #[y_start:y_end,x_start:x_end]
                # print(x,y,x+w,y+h)
                # os.path.join(path,file)
                cv2.imwrite(os.path.join(path, name_path+str(i)+'.jpg'), img1)
                # cv2.imwrite(path,file)

                i=i+1
        cv2.imshow('video',img)
        # t1_stop = perf_counter_ns()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # if (t1_stop == 5):
        #     pg.press('q')
    cap.release()
    cv2.destroyAllWindows()
    return i

