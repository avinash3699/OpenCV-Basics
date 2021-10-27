import cv2

video = cv2.VideoCapture("All over in 10 seconds.mp4")

if not video.isOpened():
    print("Error Playing the Video")
        
while video.isOpened():
    
        flag, frame = video.read()
        
        if flag == True:
            cv2.imshow("All over in 10 seconds", frame)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        else:
            break
   
video.release()
cv2.destroyAllWindows()