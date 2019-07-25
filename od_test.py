# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:24:57 2019

@author: Sunny
"""

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tensorflow as tf
import cv2
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import pandas as pd
import math

os.chdir('C:/Users/Sunny/Anaconda3/envs/tf_GPU/Lib/site-packages/models/research/object_detection')
sys.path.append("..")

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

fileList = []
folderCount = 0
rootdir = 'D:/test_mAP/img'

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        f = os.path.join(root,file)
        fileList.append(f)

MODEL_NAME = 'egg0716_fix'    #[30,21]  best
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('images', 'egg_1234.pbtxt')
NUM_CLASSES = 4

#Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

#category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        
        for i in range(len(files)):
            image = cv2.imread(rootdir+'/'+files[i])
            image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#            image = Image.open(rootdir+'/'+files[i])
#            image_np = load_image_into_numpy_array(image)
            image_np_expanded = np.expand_dims(image_bgr, axis=0)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
           # Visualization of the results of a detection.
                
           ###########
#            boxes = np.squeeze(boxes)
#            scores = np.squeeze(scores)
#            classes = np.squeeze(classes)
#
#            indices = np.argwhere(classes == 1)
#            boxes = np.squeeze(boxes[indices])
#            scores = np.squeeze(scores[indices])
#            classes = np.squeeze(classes[indices])
        ###########
            vis_util.visualize_boxes_and_labels_on_image_array(
                    image,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=1,
                    min_score_thresh=.7)
            cv2.imwrite('D:/test_mAP/img_result_0716_fix/'+files[i], image)
            print('saved '+files[i])
            print('Object detection done')
            box = np.squeeze(boxes)
            fp = open('D:/test_mAP/img_result_0716_fix/'+files[i].replace('jpg','txt'),'w')
            for i in range (18):
                if classes[0,i] == 1.0:
                    clas = 'brown_egg'
                elif classes[0,i] == 2.0:
                    clas = 'white_egg'
                elif classes[0,i] == 3.0:
                    clas = 'defect'
                elif classes[0,i] == 4.0:
                    clas = 'empty'
                
                if scores[0,i]==0.0:
                    break
                else:
                    fp.write('{} {} {} {} {} {}\n'.format(
                            clas,round(scores[0,i],7),
                            int(box[i,0]*480),
                            int(box[i,1]*640),
                            math.ceil(box[i,2]*480),
                            math.ceil(box[i,3]*640)))
                    print(clas,scores[0,i],
                          int(box[i,0]*480),
                          int(box[i,1]*640),
                          math.ceil(box[i,2]*480),
                          math.ceil(box[i,3]*640))
            fp.close()
'''
def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
#Detection
# For the sake of simplicity we will use only 2 images:
# image1.jpg
# image2.jpg
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = 'D:/egg0703'
os.chdir(PATH_TO_TEST_IMAGES_DIR)
TEST_IMAGE_DIRS = os.listdir(PATH_TO_TEST_IMAGES_DIR)

#PATH_TO_TEST_IMAGES_DIR = 'test_images2'
#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'frame{}.jpg'.format(i)) for i in range(2176, 2179) ]


# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)

output_image_path = ('D:/test_result/egg0709_2')
output_csv_path = ('D:/test_result/egg0709_2')

for image_folder in TEST_IMAGE_DIRS:   
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            TEST_IMAGE_PATHS = os.listdir(os.path.join(image_folder))
#            TEST_IMAGE_PATHS = 'D:/egg0703/egg/'+image_folder
            os.makedirs(output_image_path+image_folder)
            data = pd.DataFrame()
            for image_path in TEST_IMAGE_PATHS:
                image = Image.open(image_folder + '//'+image_path)
#                image = Image.open(image_folder + '//'+image_path)
                width, height = image.size
                # the array based representation of the image will be used later in order to prepare the
                # result image with boxes and labels on it.
                image_np = load_image_into_numpy_array(image)
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                        [detection_boxes, detection_scores, detection_classes, num_detections],
                        feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.
                vis_util.visualize_boxes_and_labels_on_image_array(
                        image_np,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)
                #write images
                #保存识别结果图片
                cv2.imwrite(output_image_path+image_folder+'\\'+image_path.split('\\')[-1],image_np)
                
                s_boxes = boxes[scores > 0.5]
                s_classes = classes[scores > 0.5]
                s_scores=scores[scores>0.5]
                
                #write table
                #保存位置坐标结果到 .csv表格
                for i in range(len(s_classes)):
                    newdata= pd.DataFrame(0, index=range(1), columns=range(7))
                    newdata.iloc[0,0] = image_path.split("\\")[-1].split('.')[0]
                    newdata.iloc[0,1] = s_boxes[i][0]*height  #ymin
                    newdata.iloc[0,2] = s_boxes[i][1]*width     #xmin
                    newdata.iloc[0,3] = s_boxes[i][2]*height    #ymax
                    newdata.iloc[0,4] = s_boxes[i][3]*width     #xmax
                    newdata.iloc[0,5] = s_scores[i]
                    newdata.iloc[0,6] = s_classes[i]
    
                    data = data.append(newdata)
                data.to_csv(output_csv_path+image_folder+'.csv',index = False)
'''


