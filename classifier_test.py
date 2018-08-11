#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu August  1 10:30:04 2018

@author: crunch
测试过程
"""
import numpy as np
import os
import argparse
from keras.models import load_model
import time
from keras.applications.imagenet_utils import preprocess_input
from scipy.misc import imread
from scipy.misc import imresize
import argparse

patch_size = (224,224)

path = os.path.join('data','test')         #### 测试集路径
imgpaths = os.listdir(path)  #### 得到这个路径下所有照片
batch_size = len(imgpaths)

def Predict(args):
    model = load_model(args.model)
    inputs = []
    for i in range(batch_size):
        print(imgpaths[i])
        img = imread(os.path.join(path,imgpaths[i])).astype('float32')
        img = imresize(img, patch_size).astype('float32')
        inputs.append(preprocess_input(img))
    inputs = np.array(inputs)
    preds = model.predict(inputs, batch_size=batch_size, verbose=1) ####　得到属于各类的概率
    print(preds)
    results = np.argmax(preds, axis=1) #### 概率最大的那个位置坐标及为类别
    print(results)

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("-model",required=True)
    args = parse.parse_args()
    starttime = time.time()
    Predict(args)
    endtime = time.time()
    runtime = endtime - starttime
    print("runtime is:",runtime)
