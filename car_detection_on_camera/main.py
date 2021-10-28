#!/usr/bin/python3.6
from modules.car_detection import CarDetection
from modules.save_img import save_img
from modules.get_img import Camera
import cv2
import numpy as np
from concurrent import futures
import os

def main():
    car_detection = CarDetection()
    #data_send = DataSendToFTP()
    camera = Camera()
    max_frame = 30
    c = 0
    frame_list = []
    flag = False
    
    executor = futures.ThreadPoolExecutor(max_workers=20)
        
    try:
        while True:
            frame = camera.get_img()
            cv2.imshow("cam",cv2.resize(frame,(480,270)))
            result = car_detection.detect(frame)
            c += 1
            if result == True:
                c = 0
                frame_list.append(frame)
                flag = True
                if max_frame == len(frame_list):
                    frame_list.pop(0)

            if result == False and flag == True and c==2:
                imgs_len = len(frame_list)
                indexes = np.linspace(imgs_len-1, 0, min(10,imgs_len), dtype = 'int')
                a = executor.submit(fn=save_img, exist_img_list=frame_list, indexes = indexes)
                flag = False
                frame_list = []
                c = 0

            print(len(frame_list))
    except:
        os.system("reboot")


if __name__ == "__main__":
    main()
