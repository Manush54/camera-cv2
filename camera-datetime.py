import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font=cv2.FONT_HERSHEY_SIMPLEX
       #text='Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))				to write height,width on camera
       dt=str(datetime.datetime.now())
       frame=cv2.putText(frame,dt,(10,50),font,1,(123,456,789),5)
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()