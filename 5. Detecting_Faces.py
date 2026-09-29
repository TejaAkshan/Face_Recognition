import face_recognition as fr
import cv2

image = fr.load_image_file("Sample Image 2.jpg")
locations = fr.face_locations(image)
bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
for face in locations:
    top, right, bottom, left = face
    cv2.rectangle(bgr, (left, top), (right, bottom), (0, 0, 0), 2)

cv2.imshow("Faces Found: ", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
