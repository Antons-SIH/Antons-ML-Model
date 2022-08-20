"""
Output of the classify function:
    bool -> PAN = True/False
    bool -> Aadhar = True/False
    list -> Coordinates = list of coordinates (will be used for cropping), will return None if neither are True

pass the path of the original image to the classify function
"""

import torch


def classify(path):
    model = torch.hub.load('/Users/aditya_gitte/Projects/SIH/ML_Model/Classification/yolov5', 'custom', source='local', path='/Users/aditya_gitte/Projects/SIH/ML_Model/Classification/best.pt',force_reload=True)  # loads the custom trained model
    classes = model.names  # class names in string format
    print(classes)
