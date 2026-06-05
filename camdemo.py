import cv2 
import random
cam=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
              
    flag,image=cam.read()
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces=cascade.detectMultiScale(gray_image,1.1,5)
    print(faces)

    # for x,y,w,h  in faces:
    if len(faces)>0:
         x,y,w,h=faces[0] 
         cv2.rectangle(image,(x,y),(x+w,y+h),(255,100,0),2)


    cv2.imshow("myimage",image)
    k=cv2.waitKey(2)
    
    if k==ord('q'):
        break
    if k==ord('s'):
        cropped=image[y:y+h,x:x+w]
        cropped=cv2.resize(cropped,(300,300))
        index=random.randint(1,100)
        path=f"./dataset/2/person{index}.jpg"

        cv2.imwrite(path,cropped)

cam.release()
# haarcasdeClassifier
# viola jones method


