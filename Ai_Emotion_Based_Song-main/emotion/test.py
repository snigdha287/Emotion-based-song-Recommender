import numpy as np
import pandas as pd
import os 
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
from tensorflow.keras.applications import VGG16, InceptionResNetV2
from keras import regularizers
from tensorflow.keras.optimizers import Adam, RMSprop,SGD, Adamax
import emotion as e
# model= tf.keras.models.Sequential()


def load_file(path):
    totalFiles = 0
    totalDir = 0
    for base, dirs, files in os.walk(path):
        print('Searching in : ',base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    return  totalFiles,totalDir


# print('Total number of files',totalFiles)
# print('Total Number of directories',totalDir)
# print('Total:',(totalDir + totalFiles))



# res = {'Angry': 0, 'Disgust': 0, 'Fear': 0, 'Happy': 0, 'Neutral': 0, 'Sad': 0, 'Surprise': 0}

def predict(model,file_name,count,res):
    for i in range(count):
        img = image.load_img(file_name+str(i)+".jpg",target_size = (48,48),color_mode = "grayscale")
        img = np.array(img)
            # print(plt.imshow(img))
            # print(img.shape)
        label_dict = {0:'Angry',1:'Happy',2:'Neutral',3:'Sad'}

        img = np.expand_dims(img,axis = 0) #makes image shape (1,48,48)
        img = img.reshape(1,48,48,1)
        result = model.predict(img)
        result = list(result[0])
        img_index = result.index(max(result))
        res[label_dict[img_index]] = res[label_dict[img_index]] + 1
        # print(label_dict[img_index]," -> ","./img/face"+str(i)+".jpg")
        os.remove(file_name+str(i)+".jpg")
    return res
def predict_image(model,path,res):

    img = image.load_img(path,target_size = (48,48),color_mode = "grayscale")
    img = np.array(img)
            # print(plt.imshow(img))
            # print(img.shape)
    label_dict = {0:'Angry',1:'Happy',2:'Neutral',3:'Sad'}

    img = np.expand_dims(img,axis = 0) #makes image shape (1,48,48)
    img = img.reshape(1,48,48,1)
    result = model.predict(img)
    result = list(result[0])
    img_index = result.index(max(result))
    res[label_dict[img_index]] = res[label_dict[img_index]] + 1
        # print(label_dict[img_index]," -> ","./img/face"+str(i)+".jpg")
    return res

