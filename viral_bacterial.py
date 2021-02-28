#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:32:49 2021

Code base from https://www.kaggle.com/madz2000/pneumonia-detection-using-cnn-92-6-accuracy

@author: Aaron Gregory
"""

from keras.models import model_from_json
import numpy
from PIL import Image 

class_names = ["Pneumonia", "Normal"]

# load json and create model
json_file = open('../weights/viral_bacterial.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("../weights/viral_bacterial.h5")

def is_normal(xray_img):
    """
    Returns 1 if xray_img shows a healthy xray, 0 else
    """
    resized = xray_img.resize((150, 150))
    open_cv_image = numpy.array(resized.convert('L')) / 255
    open_cv_image = open_cv_image.reshape(-1,150,150,1)
    output = loaded_model.predict_classes(open_cv_image)
    return output[0,0]

if __name__ == "__main__":
    image = Image.open("./c0.png")
    print(class_names[is_normal(image)])
    
    image = Image.open("./c1.png")
    print(class_names[is_normal(image)])
    
    image = Image.open("./n0.png")
    print(class_names[is_normal(image)])
    
    image = Image.open("./n1.png")
    print(class_names[is_normal(image)])
    
    image = Image.open("./v0.png")
    print(class_names[is_normal(image)])
    
    image = Image.open("./v1.png")
    print(class_names[is_normal(image)])

