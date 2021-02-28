#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:32:49 2021

Code base from https://www.kaggle.com/arunlukedsouza/covid-19-chest-x-ray-classification-with-resnet-18

@author: Aaron Gregory
"""

import torch
import torchvision
from PIL import Image
from torch.utils.data import DataLoader

class_names = ['Normal', 'Viral', 'COVID-19']

model = torch.load("../weights/covid_resnet18.dat")

transform = torchvision.transforms.Compose([
    # Converting images to the size that the model expects
    torchvision.transforms.Resize(size=(224,224)),
    # Converting to tensor
    torchvision.transforms.ToTensor(),
    # Normalizing the data to the data that the ResNet18 was trained on
    torchvision.transforms.Normalize(mean = [0.485, 0.456, 0.406],
                                      std = [0.229, 0.224, 0.225])
])

def has_pneumonia(xray_img):
    """
    Returns 0 if xray_img shows a healthy xray, 1 if viral pneumonia, and 2 if covid
    """
    processed = transform(xray_img.convert('RGB'))
    data = DataLoader(dataset=[processed], batch_size=1)
    inpt = next(iter(data))
    output = model(inpt)
    _, pred = torch.max(output, 1)
    return pred[0]

if __name__ == "__main__":
    image = Image.open("./c0.png")
    print(class_names[has_pneumonia(image)])
    
    image = Image.open("./c1.png")
    print(class_names[has_pneumonia(image)])
    
    image = Image.open("./n0.png")
    print(class_names[has_pneumonia(image)])
    
    image = Image.open("./n1.png")
    print(class_names[has_pneumonia(image)])
    
    image = Image.open("./v0.png")
    print(class_names[has_pneumonia(image)])
    
    image = Image.open("./v1.png")
    print(class_names[has_pneumonia(image)])
