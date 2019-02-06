import cv2
import time

video_capture = cv2.VideoCapture(0)

while True:
    time.sleep(1)
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2.imwrite('static/captured_image.png', frame)

video_capture.release()
cv2.destroyAllWindows()