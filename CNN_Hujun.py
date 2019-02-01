# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:22:42 2019

@author: sunny
"""

# https://cloud.tencent.com/developer/article/1086770
import os
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # matplotlib speed up
#import pyqtgraph as pg
from sklearn.model_selection import train_test_split
from sklearn import metrics

# data path
data_dir = "D:\\Tene\\train448"
# train or test
train = True

model_path = "D:\\Tene\\model\\train448_0201"

# read image and label to numpy matrix
def read_data(data_dir):
    datas = []
    labels = []
    fpaths = []
    for fname in os.listdir(data_dir):
        fpath = os.path.join(data_dir, fname)
        fpaths.append(fpath)
        image = Image.open(fpath)
        data = np.array(image) / 255.0
        label = int(fname.split("_")[0])
        datas.append(data)
        labels.append(label)

    datas = np.array(datas)
    labels = np.array(labels)

    print("shape of datas: {}\tshape of labels: {}".format(datas.shape, labels.shape))
    return fpaths, datas, labels


fpaths, datas, labels = read_data(data_dir)
#train_X, test_X, train_y, test_y = train_test_split(
#        datas, labels, test_size = 0.1)
num_classes = len(set(labels))

# setting placeholder for saving input datas and labels
datas_placeholder = tf.placeholder(tf.float32, [None, 448, 448, 3])
labels_placeholder = tf.placeholder(tf.int32, [None])

# 0.25 for training，0 for testing 
dropout_placeholdr = tf.placeholder(tf.float32)

# setting CNN
conv0 = tf.layers.conv2d(inputs=datas_placeholder, filters=20, kernel_size=5, activation=tf.nn.relu)
pool0 = tf.layers.max_pooling2d(inputs=conv0, pool_size=[2, 2], strides=[2, 2])

conv1 = tf.layers.conv2d(inputs=pool0, filters=40, kernel_size=4, activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=[2, 2])

# transfer 3d vector to 1d
flatten = tf.layers.flatten(pool1)

# 全连接层，转换为长度为100的特征向量
fc = tf.layers.dense(flatten, 400, activation=tf.nn.relu)

# for prevent overfitting 
dropout_fc = tf.layers.dropout(fc, dropout_placeholdr)

# 未激活的输出层
logits = tf.layers.dense(dropout_fc, num_classes)

predicted_labels = tf.arg_max(logits, 1)

# use cross entropy setting loss
losses = tf.nn.softmax_cross_entropy_with_logits(
    labels=tf.one_hot(labels_placeholder, num_classes),
    logits=logits
)
mean_loss = tf.reduce_mean(losses)

optimizer = tf.train.AdamOptimizer(learning_rate=1e-2).minimize(losses)

# for saving or loading model
saver = tf.train.Saver()
# gpu
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
#sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
with tf.Session() as sess:

    if train:
        print("Training mode")
        # initial
        sess.run(tf.global_variables_initializer())
        sess(config=tf.ConfigProto(gpu_options=gpu_options))
        # setting inputs and labels
        train_feed_dict = {
            datas_placeholder: datas,
#            datas_placeholder: train_X,
            labels_placeholder: labels,
#            labels_placeholder: train_y,
            dropout_placeholdr: 0.25
        }
        # iteration
        for step in range(150):
            _, mean_loss_val = sess.run([optimizer, mean_loss], feed_dict=train_feed_dict)

            if step % 10 == 0:
                print("step = {}\t mean loss = {}".format(step, mean_loss_val))
        saver.save(sess, model_path)
        print("Training completed, saving model to {}".format(model_path))
    else:
        print("Testing mode")
        saver.restore(sess, model_path)
        print("Model path: {}".format(model_path))
        
        # setting label dict.
        label_name_dict = {
            0: "santa",
            1: "bug",
            2: "blue",
            3: 'red',
            4: 'sis',
#             0:'14881', 1:'14882', 2:'14883', 3:'14884', 4:'14885',
#             5:'155431', 6:'155432', 7:'155433', 8:'155434', 9:'155435',
#             10:'54341', 11:'54342', 12:'54343', 13:'54344',
#             14:'55391', 15:'55392', 16:'55393', 17:'55394', 18:'55395',
#             19:'55751', 20:'55752', 21:'55753', 22:'55754', 23:'55755'
        }
        # setting inputs and labels, dropout = 0 when testing mode
        test_feed_dict = {
            datas_placeholder: datas,
#            datas_placeholder: test_X,
            labels_placeholder: labels,
#            labels_placeholder: test_y,
            dropout_placeholdr: 0
        }
        # predict labels
        predicted_labels_val = sess.run(predicted_labels, feed_dict=test_feed_dict)
        
        # build real label list and predicted label list
        real_label_list = []
        predicted_label_list = []
        for fpath, real_label, predicted_label in zip(fpaths, labels, predicted_labels_val):
            # 将label id转换为label名
##            real_label_name = label_name_dict[real_label]
##            predicted_label_name = label_name_dict[predicted_label]
            real_label_list.append(real_label)
#            real_label_name.append(list(label_name_dict.values()).index(str(real_label)))
            predicted_label_list.append(predicted_label)
#            predicted_label_name.append(predicted_label)
        
        plt.figure(figsize=(50,10), linewidth=0.9)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        plt.xlabel('samples',fontsize=40)
        plt.ylabel('label',fontsize=40)
        for i in range(len(labels)):
            p1 = plt.scatter(i,real_label_list[i], color='blue', s=200)
            p2 = plt.scatter(i,predicted_label_list[i], color='red', s=150)
        plt.legend([p1,p2],['real','predicted'],loc='upper right',fontsize=40)
        plt.savefig('D:\\Tene\\{x}.png'.format(x=model_path.split('\\')[-1]))
        plt.show()
        accuracy = metrics.accuracy_score(real_label_list, predicted_label_list)
        print('Accuracy: ',accuracy)
        

            
            
            
        
            
