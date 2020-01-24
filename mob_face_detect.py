import cv2
import requests
import numpy as np

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    
    url = "http://192.168.43.1:8080/shot.jpg"
    # url connect
    geturl = requests.get(url)
    # get photo access
    photoweb = geturl.content
    # convet byte to bytearray
    photobyte = bytearray(photoweb)
    # convert bytearray to 1d array
    image = np.array(photobyte)
    # convert 1d to 3d array
    frame = cv2.imdecode(image,-1)
    frame = cv2.resize(frame,(600,600))
    faces = face_detect.detectMultiScale(frame)
    
    if faces is not ():

        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        
        photo = cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,0,255),4)
        photo = photo[y-20:y+h+20 , x-20:x+w+20]
    
    
    cv2.imshow("myCam",frame)
    if cv2.waitKey(1) == 13:
        break
cv2.imwrite("found.png",photo)
cv2.destroyAllWindows()
