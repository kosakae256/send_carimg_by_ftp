from modules.car_detection import CarDetection
from modules.ftp_send_img import DataSendToFTP
from modules.get_img import Camera
import cv2


def main():
    car_detection = CarDetection()
    data_send = DataSendToFTP()
    camera = Camera()

    while True:
        frame = camera.get_img()
        cv2.imshow("cam",frame)
        result = car_detection.detect(frame)
        if result == True:
            data_send.send(frame)

if __name__ == "__main__":
    main()