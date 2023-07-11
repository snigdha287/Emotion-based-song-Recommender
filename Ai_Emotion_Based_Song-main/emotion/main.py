import emotion as e
import test
from keras.models import load_model
import cv2
import os


# model = load_model('./emo/') #saved model
# model = load_model('emotion.h5')
def loadModel():
    model_path = './emo/'
    model = load_model(model_path)
    return model

def cap_mode(path,face,cap,name_path,model,res):
    count = e.fun(path, name_path, face, cap)
    test.predict(model, file_name, count, res)
    return res

def img_upload_mode(path1,model,res):    #WE'VE TO WORK ON IT
    tot_fil = test.load_file(path1)
    for i in range(tot_fil):
        path = './test/happy/im'+str(i)+'.png'
        test.predict_image(model,path,res)
    return res

def switcher(key):
    switch = {
        0 : 'camera mode',
        1 : 'upload img',
        2 : "Exit",
        3 : "back to input"
    }
    return switch[key]
def theory():
    print( ''' 
               0 : 'camera mode',
               1 : 'upload img',
               2 : "Exit",
               3 : "back to input" 
        ''')
def resl(res):
    max = 0
    key1 = ''
    for key in res:
        if (res[key] > max):
            max = res[key]
            key1 = key
    # print(res)
    # print(key1," -> ",max)
    return key1

if __name__ == '__main__':
    model = loadModel()
    camera = 0 #default
    path = "./haarcascades/haarcascade_frontalface_alt2.xml"
    face = cv2.CascadeClassifier(path)

    cap = cv2.VideoCapture(0)
    path = './img/'  # temporary path to save images
    name_path = 'face'
    file_name = './img/face'
    path1 = './test/happy/im105.png'
    # tot_fil = test.load_file(path)
    res = {'Angry': 0, 'Happy': 0, 'Neutral': 0, 'Sad': 0}
    while True:
        theory()
        n = int(input("Enter the value : "))
        # try:
        result = switcher(n)
        if (result == 'camera mode'):
            # r1 = cap_mode(path=path, face=face, cap=cap, name_path=name_path, model=model,res=res)
            r1 = cap_mode(path, face, cap, name_path, model, res)
            print(resl(r1))
            for key in res:
                res[key] = 0

        elif (result == 'upload img'):
            # r2 = img_upload_mode(path1, model, res)
            # print(resl(r2))
            print("Currently not available ...")

        elif (result == 'Exit'):
            break
        # except Exception as e:
        #     print("please choose wisely ...")
        #


    # count = 0
    # while (True):
    #     count = e.fun(path, name_path, face, cap)
    #     print(test.predict(model,file_name,count,res))
