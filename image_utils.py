from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    img = Image.open(path)
    img_array = np.array(img)
    return img_array

def edge_detection(image):
  gray_image = np.mean(image, axis=2)
  kernelY = np.array([[1, 1, 1],
                      [0, 0, 0]
                      [-1, -1, -1]])
  kernelX = np.array([[1, 0, -1],
                      [1, 0, -1]
                      [1, 0, -1]])
  edge_y = convolve2d(gray_image, kernelY, mode='same')
  edge_x = convolve2d(gray_image, kernelX, mode='same')
  edgeMAG = np.sqrt(edge_x**2 + edge_y**2)
  return edgeMAG
