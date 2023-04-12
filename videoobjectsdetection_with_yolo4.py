# -*- coding: utf-8 -*-
"""videoObjectsDetection_with_yolo4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c8wZVg_NqPIzPeiXTfpfn6Y9ALw8F1qM

### YOLO4
"""

# !pip install opencv-python==4.5.5.64

import cv2
# from google.colab.patches import cv2_imshow
import time
import traceback
import numpy as np

"""### Loading weights and configuration file for yolov4
1. **'modelConfiguration' specifies the configuration file (yolov4-tiny.cfg)** that contains the architecture of the model, including the number of layers, filters, and other parameters.
2. **'modelWeights' specifies the pre-trained weights file (yolov4-tiny.weights)** that contains the learned parameters of the model. 
"""

#read the wieghts and cfg file openCv , readNet function automatically detects an origin framework of a 
#trained model(readNetFromCaffe, readNetFromTensorflow, readNetFromTorch, or readNetFromDarknet).
net = cv2.dnn.readNet(r"dnn_model/yolov4-tiny.weights",\
                      r"dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size = (320,320),scale = 1/255)

"""#### Read the file that contain the name of different classes(objects name)"""

classes = []
with open(r"dnn_model/classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print(classes)

"""##### Read the video file and also set the dimension of video frame

"""

cap = cv2.VideoCapture(r"video.mp4")
# setting the dimension
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

"""#### Draw the bbox and file name on video's objects"""

#as long as frame in the model
while True:
    #get frames
    ret,frame = cap.read()
    #get the bbox etc
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        #blue bbox
        cv2.rectangle(frame,(x,y),(x + w,y + h),(200,10,50),3)
        class_name = classes[class_id]
        #blue text
        cv2.putText(frame, (class_name),(x,y-10),cv2.FONT_HERSHEY_PLAIN,2,(200,10,50),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,10,50),3)
        print('classs',class_ids)
        print('scores',scores)
        print('bboxes',bboxes) 
        

        cv2.imshow('Frame1',frame)
        #delay time to update frame
        time.sleep(1.1)

    if cv2.waitKey(27) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

"""### conclusion: 
our pre trained yolo4 model working very well over traffic video to detact car trucks etc as shown above the output of video,their bbox ,class name, class id etc

"""

