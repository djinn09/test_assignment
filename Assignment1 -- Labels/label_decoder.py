import cv2
import numpy as np 

image_to_decode = cv2.imread('resources/10.png') # loading a sample encoded image


class LabelDecoder:

	def __init__(self):
		print('Decoder object created..')
### your code here