import requests
import cv2
import numpy as np

url1 ="http://192.168.43.1:8080/shot.jpg"
url2="http://192.168.137.:8080/shot.jpg"

while True:
	geturl1=requests.get(url1) 
	photoweb1=geturl1.content 
	type(photoweb1) 
	photobyte1=bytearray(photoweb1) 
	imageId1=np.array(photobyte1) 
	frame1 = cv2.imdecode(imageId1,-1) 
	
	geturl2=requests.get(url2) 
	photoweb2=geturl2.content
	type(photoweb2) 
	photobyte2=bytearray(photoweb2) 
	imageId2=np.array(photobyte2)
	frame2 = cv2.imdecode(imageId2,-1) 
	
	reframe1=cv2.resize(frame1,(400,400))
	reframe2=cv2.resize(frame2,(400,400))
	
	frame3=np.concatenate((reframe1,reframe2),axis=1)
	
	cv2.imshow("hi",frame3)
	if cv2.waitKey(1) == 13: 
		break
cv2.destroyAllWindows()
cv2.release()
