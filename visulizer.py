import numpy as np
import cv2

# Create a black image
arr=[510,400,288,176,176-112]
i=0
img = np.zeros((512,512,3), np.uint8)
print("1)Stack\n2)Queue")
x=input()
if x == 1:
    while True:
        img = cv2.rectangle(img,((512//2)-10,510),((512//2)+10,470),(0,255,0),1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Top',((512//2)+15,480), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow("image",img)
        cv2.waitKey(0)
        while True:
            print("1)push\n2)pop")
            x=input()
            if x==1:
                i=i+1
                img = cv2.rectangle(img,((512//2)-10,arr[i]),((512//2)+10,arr[i]-40),(0,255,0),1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Top',((512//2)+15,arr[i-1]-30), font, 1,(0,0,0),2,cv2.LINE_AA)
                img = cv2.arrowedLine(img, ((512//2),arr[i]), ((512//2),arr[i]+70),(0,255,0),1)
                cv2.putText(img,'Top',((512//2)+15,arr[i]-30), font, 1,(255,255,255),2,cv2.LINE_AA)
            if x==2:
                i=i-1
                img = cv2.rectangle(img,((512//2)-10,arr[i+1]),((512//2)+10,arr[i+1]-40),(0,0,0),1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Top',((512//2)+15,arr[i+1]-30), font, 1,(0,0,0),2,cv2.LINE_AA)
                img = cv2.arrowedLine(img, ((512//2),arr[i+1]), ((512//2),arr[i+1]+70),(0,0,0),1)
                cv2.putText(img,'Top',((512//2)+15,arr[i]-30), font, 1,(255,255,255),2,cv2.LINE_AA) 
            """img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
            img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)"""
            cv2.imshow("image",img)
            cv2.waitKey(0)
        cv2.destroyAllWindows()