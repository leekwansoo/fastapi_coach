import cv2
import numpy as np

async def stack_video(file_paths):
    
    video_path1 = file_paths[0]
    video_path2 = file_paths[1]
    print(video_path1, video_path2)
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)



    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = round(cap1.get(cv2.CAP_PROP_FPS))
    fps2 = round(cap2.get(cv2.CAP_PROP_FPS))
    print(fps, fps2)
    w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(w,h)
    out = cv2.VideoWriter('%s_stacked.avi' % (video_path1.split('.')[0]), fourcc, fps, (w*2, h))
    file_name = video_path1.split('.')[0] + "_stacked.avi"

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break
        #frame2Resized = cv2.resize(frame2,(frame1.shape[0],frame1.shape[1]))

        # ---- Option 1 ----
        #numpy_vertical = np.vstack((frame1, frame2))
        frame1 = cv2.resize(frame1, (w,h))
        frame2 = cv2.resize(frame2, (w,h))
        numpy_horizontal = np.hstack((frame1, frame2))

        # ---- Option 2 ----
        #numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)
        #numpy_horizontal_concat = np.concatenate((frame1, frame2), axis=1)

        #cv2.imshow("Result", numpy_horizontal)

        out.write(numpy_horizontal)
        
        #cv2.waitKey(100)

    #cv2.destroyAllWindows()

    return (file_name)




