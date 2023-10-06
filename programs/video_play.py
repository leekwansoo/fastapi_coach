import cv2
import numpy as np

def play_video(file_path):
    
    print(file_path)
    video_path = file_path
    cap1 = cv2.VideoCapture(video_path)
   
    fps = round(cap1.get(cv2.CAP_PROP_FPS))
    print(fps)
    w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(w,h)


    while True:
        ret1, frame1 = cap1.read()
       
        if not ret1:
            break
        #frame2Resized = cv2.resize(frame2,(frame1.shape[0],frame1.shape[1]))

        # ---- Option 1 ----
        #numpy_vertical = np.vstack((frame1, frame2))
        frame1 = cv2.resize(frame1, (w,h))
         
        # ---- Option 2 ----
        #numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)
        #numpy_horizontal_concat = np.concatenate((frame1, frame2), axis=1)

        cv2.imshow("frame1", frame1)
        
        cv2.waitKey(100)
        
    cv2.destroyAllWindows()

    return ()