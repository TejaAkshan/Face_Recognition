import face_recognition as fr
import matplotlib.pyplot as plt 
import cv2

image = fr.load_image_file("Sample Image.jpg")
plt.imshow(image)
plt.show()
