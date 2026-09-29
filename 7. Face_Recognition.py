import face_recognition as fr
import cv2

image = fr.load_image_file("Akshan.jpg")
locations = fr.face_locations(image)
encode = fr.face_encodings(image, locations)
bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
 
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access the camera")
    exit()
while True:
    ret, frame = camera.read()
    if not ret:
        print("Frame is not detected")
        break
    
    cv2.imshow("Camera Live feed", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("Captured Image.jpg", frame)
        print("Image captured successfully")
    elif key == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

cap_image = fr.load_image_file("Captured Image.jpg")
locations2 = fr.face_locations(cap_image)
encode2 = fr.face_encodings(cap_image, locations2)
bgr2 = cv2.cvtColor(cap_image, cv2.COLOR_RGB2BGR)

if len(encode2) == 0:
    print("No faces are detected")

else:
    result = fr.compare_faces(encode, encode2[0])
    if result[0]:
        print("MATCH!!!")
    else:
        print("NOT MATCH!!!")