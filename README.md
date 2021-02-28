# R-AGI
R-AGI: Radiology Artificial General Intelligence. This is a system for automatically locating and diagnosing anomalies in chest x-rays, currently capable of destinguishing between viral and bacterial pneumonia with >90% accuracy.

## Design
R-AGI conducts both global and local analysis. First a pair of pneumonia classification models are called to determine the presence and type of pneumonia shown in the x-ray, respectively. These models are based on designs from Kaggle, given [here](https://www.kaggle.com/arunlukedsouza/covid-19-chest-x-ray-classification-with-resnet-18) and [here](https://www.kaggle.com/madz2000/pneumonia-detection-using-cnn-92-6-accuracy). If pneumonia is found in the x-ray, we plan to call a localization model similar to [AE-CNN](https://github.com/ekagra-ranjan/AE-CNN). This would produce a heatmap of where the pneumonia is located in the chest cavity; however, we have not yet finished training an AE-CNN, so in the meantime we use a simpler bounding box system.

## Use
Running 'ragiface.py' will bring up a GUI where the user can browse for a local x-ray image. After an image is selected, processing it will give three pieces of output: 1) whether any pneumonia was detected, 2) what type of pneumonia it was, and 3) if it could be localized, a bounding box will be shown.
