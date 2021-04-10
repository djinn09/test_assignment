import cv2
import numpy as np


box = cv2.imread('resources/box.png') # loading the box image
circle = cv2.imread('resources/circle.png') # loading the circle image
dot = cv2.imread('resources/dot.png') # loading the dot image


# decimal to binary dictionary for reference
binary_dict = {
    '0': [0, 0, 0, 0],
    '2': [0, 0, 1, 0],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '14': [1, 1, 1, 0],
    '15': [1, 1, 1, 1]
}

class LabelEncoder:

	def __init__(self):
		print('Encoder object created..')
### YOur code here