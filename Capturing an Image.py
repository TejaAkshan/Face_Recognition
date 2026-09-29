import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access the camera")
    exit()
while True:
    ret, frame = camera.read()
    if not ret:
        print("Cant revieve frame")
        break
    cv2.imshow("Live Camera feed", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("Captured an Image.jpg", frame)
        print("Image Captured Successfully")

    elif key == ord('q'):
        exit()