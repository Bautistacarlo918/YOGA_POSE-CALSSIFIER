import cv2 as cv
import mediapipe as mp
import numpy as np

#Initialize drawing
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#Initialize camera
cap = cv.VideoCapture (0)








if __name__ == "__main__" :
    
    #Set the pipe
    with mp_pose.Pose(min_detection_confidence = 0.5 ,
                    min_tracking_confidence = 0.5) as pose:
    #Vid
        while cap.isOpened():
            ret , frame = cap.read()

            image = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            #detect
            results = pose.process(image)

            image.flags.writeable = True
            image = cv.cvtColor (image , cv.COLOR_RGB2BGR)

            #render
            mp_drawing.draw_landmarks(image , results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color = (255,255,255) , thickness = 2 , circle_radius = 2), #dots
                                    mp_drawing.DrawingSpec(color = (255,255,255) , thickness = 2 , circle_radius = 2) #lines
                                    )
            #Extract Landmark
            try:
                landmarks = results.pose_landmarks.landmark
                # print (landmarks)
                print (len(landmarks))
            except:
                pass

            cv.imshow ("Camera" , image)

            if cv.waitKey(1) & 0xff == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()
