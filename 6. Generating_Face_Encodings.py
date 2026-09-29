import face_recognition as fr
import cv2

image = fr.load_image_file("Sample Image.jpg")
locations = fr.face_locations(image)
encode = fr.face_encodings(image, locations)
bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
for i in range(len(locations)):
    top, right, bottom, left = locations[i]
    encoding = encode[i]
    cv2.rectangle(bgr, (left, top), (right, bottom), (0, 0, 0), 2)
    print("Encoding for the face: ", encoding)
cv2.imshow("Face with encodings: ", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()