from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the `pass` with your code

def edge_detection(image):
    pass # Replace the `pass` with your code





from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    """
    טוענת תמונה מהנתיב הנתון וממירה אותה לגווני אפור (Grayscale)
    כדי שנוכל לבצע עליה חישובים מתמטיים בקלות.
    """
    img = Image.open(path).convert('L')
    return np.array(img)

def edge_detection(image):
    """
    מזהה קצוות בתמונה באמצעות שימוש בקרנל (Kernel) של Sobel.
    """
    kernel_x = np.array([[-1, 0, 1], 
                         [-2, 0, 2], 
                         [-1, 0, 1]])
    
    kernel_y = np.array([[-1, -2, -1], 
                         [ 0,  0,  0], 
                         [ 1,  2,  1]])
    
    grad_x = convolve2d(image, kernel_x, mode='same')
    grad_y = convolve2d(image, kernel_y, mode='same')
    
    edge_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    
    edge_magnitude = (edge_magnitude / edge_magnitude.max()) * 255
    
    return edge_magnitude.astype(np.uint8)
