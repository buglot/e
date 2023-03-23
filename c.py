import cv2
import uuid
import os
cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite(os.path.join("mask",f"mask_{uuid.uuid1()}.jpg"),frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap objectqqqqqqqq
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()