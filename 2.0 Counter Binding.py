import cv2

import numpy as np



img=cv2.imread('light.png') #0-gray -1 -nochange , 1 color

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #Approximating more boundry points for more accuracy
#Chain-approx-simple - searching for minimal boundry points for identification (avoid redundent points)

cnt=contours[0]

x,y,w,h=cv2.boundingRect(cnt)

cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


#rotated rectangle
rect=cv2.minAreaRct(cnt)
point=cv2.boxPoints(rect)

poins=np.int0(points)
cv2.drawContours(img,[points],0,(0,0,255),2)
#print(rect)

#circle

(x,y),radius=cv2.minEnclosingCircle(cnt)
x=int(x)
y=int(y)
radius=int(radius)

cv2.circle(img,(x,y),radius,(255,0,0),2)

#ellipse
ellipse=cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,255),2)
ABOUT
cv2.imshow('IMG',img)
cv2.waitKey(100)


