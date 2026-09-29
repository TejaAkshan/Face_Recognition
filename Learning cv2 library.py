import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to open Camera")
    exit()
while True:
    ret, frame = camera.read()
    if not ret:
        print("Cant recieve frame")
        break
    cv2.imshow("Live Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()