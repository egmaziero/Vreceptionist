import cv2
import time


class Camera():

    @staticmethod
    def get_frame():
        _, frame = cv2.VideoCapture(0).read()
        small_image = cv2.resize(frame, (0,0), fx=0.3, fy=0.3)
        cv2.VideoCapture(0).release()
        cv2.destroyAllWindows()
        return cv2.imencode('.jpg', small_image)[1].tobytes()
