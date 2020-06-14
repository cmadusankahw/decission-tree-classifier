import cv2


img=cv2.imread('light.png',0) #0-gray -1 -nochange , 1 color
cv2.imshow('IMG',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)

ret,contours,hierarchy=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #Approximating more boundry points for more accuracy
#Chain-approx-simple - searching for minimal boundry points for identification (avoid redundent points)

cnt=contours[0]

for val in cnt:
    (x,y)=val[0]
    cv2.circle(img,(x,y),10,(0,255,0),-1)

cv2.imshow('IMG',img)