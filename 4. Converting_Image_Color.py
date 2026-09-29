import face_recognition
import cv2

# Load image using face_recognition
image = face_recognition.load_image_file("Sample Image.jpg")

# Convert from RGB (face_recognition) to BGR (OpenCV uses this)
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Shows the image
cv2.imshow("Loaded Image", image_bgr)
cv2.waitKey(0) # It waits for 0 seconds in this case
cv2.destroyAllWindows() # This function closes all the windows that were opened using cv2.imshow() function

