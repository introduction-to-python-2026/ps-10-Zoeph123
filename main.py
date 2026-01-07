import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import median
from skimage.morphology import ball
from PIL import Image

test = load_image("swimmer.jpg")
clean_image = median(test, ball(3))
edge_test = edge_detection(clean_image)
threshold_value = 50
edge_binary = edge_test > threshold_value

plt.figure(figsize=(10, 5))
plt.imshow(edge_binary, cmap='gray')
plt.axis('off')
plt.show()


edge_image = Image.fromarray((edge_binary * 255).astype(np.uint8)) 
edge_image.save("my_edges.png")
