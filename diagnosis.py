#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:38:13 2021

@author: Aaron Gregory
"""

from pneumonia_detection import has_pneumonia
from viral_bacterial import is_normal
from PIL import Image, ImageDraw

rect = [0.23, 0.2, 0.5, 0.8]


def localize(xray_img):
    """
    This would normally overlay a heat map or set of bounding boxes
    onto xray_img showing where anSomalies are, but we don't have
    time for that, so we're faking data.
    
    Draws a rectangle onto xray_img, showing the region of v0.png
    which contains pneumonia. Returns the resulting image.
    """
    img_rgb = xray_img.convert("RGB").resize((200, 200))
    img = ImageDraw.Draw(img_rgb)
    w = img_rgb.size[0]
    img.rectangle([(int(w * rect[0]), int(w * rect[1])), (int(w * rect[2]), int(w * rect[3]))], fill=None,
                  outline="#ff3333")
    return img_rgb


# API is as follows:
# - Process_xray (xray_img): That'll be the function that Josh will pass the image of X-ray to
# - Global_Check(True/False): That'll be a function you call to say whether you want to display check mark or x-mark once global health check result comes back - if it is done, you pass check, if code crashes, x-mark
# - Locate_anomalies(True/False): That'll be a function you call to say whether you want to display check mark or x-mark for locate anamolies success/fail
# - results_text(text): you'll call this function with a string you want to have in text widget
# - result_img(img): You'll call this function with an image that Josh will display beside text widget
def Process_xray(xray_img, global_check, locate_anomalies, results_text, result_img, add_text):
    """
    This function should be called by the GUI to begin diagnosis.
    xray_img should be a chest xray to diagnose, in a PIL format.
    All other arguments should be callback functions matching the API.
    """
    # First model. Trustworthy for detecting presence of pneumonia, but not type.
    normalcy_code = is_normal(xray_img)
    # Second model. Has some false positives, but gives types of pnuemonia well.
    pneumonia_code = has_pneumonia(xray_img)

    if normalcy_code == 1:  # indicates healthy xray
        global_check(True)
        result_img(xray_img.resize((200, 200)))  # no anomalies
        locate_anomalies(False)
        if pneumonia_code == 0:  # models agree
            add_text("Healthy")
        else:  # probably a false positive
            add_text("Pneumonia unlikely")
    else:  # indicates pneumonia
        global_check(True)
        result_img(localize(xray_img))  # show problem region
        locate_anomalies(True)
        if pneumonia_code == 0:  # probably a false negative
            add_text("Pneumonia likely")
        elif pneumonia_code == 1:  # not covid
            add_text("Viral pneumonia detected")
        else:  # not covid
            add_text("COVID-19 detected")


def xray_process(img, add_text, insert_img):
    def f1(x):
        add_text("Global_Check = " + str(x))

    def f2(x):
        add_text("Locate_anomalies = " + str(x))

    def f3(x):
        add_text("results_text= " + str(x))

    def f4(x):
        rect = [0.6, 0.4, 0.8, 0.75]
        insert_img(x)
        print('got something here')
        pass
        # add_text("result_img ")

    Process_xray(img, f1, f2, f3, f4, add_text)

# if __name__ == "__main__":
#     # a bunch of functions to use as callbacks
#
#
#
#     # how the calls should go from the GUI:
#
#     print("\n\nCASE 1: VIRAL PNEUMONIA\n\n")
#     rect = [0.23, 0.2, 0.5, 0.8]
#     image = Image.open("./v0.png") # viral pneumonia
#     Process_xray(image, f1, f2, f3, f4)
#
#     print("\n\nCASE 2: HEALTHY\n\n")
#     image = Image.open("./n0.png") # healthy
#     Process_xray(image, f1, f2, f3, f4)
#
#     print("\n\nCASE 3: COVID\n\n")
#     rect = [0.6, 0.4, 0.8, 0.75]
#     image = Image.open("./c0.png") # covid
#     Process_xray(image, f1, f2, f3, f4)
