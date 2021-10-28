import cv2
import requests
import numpy as np


class Camera():
    def __init__(self):
        # video init.
        
        self.movie = cv2.VideoCapture("rtsp://192.168.1.201/live1s1.sdp")
        
        while True:
            if self.movie.isOpened():
                return
        
        
    def get_img(self):
        self.fps = int(self.movie.get(cv2.CAP_PROP_FPS)) #動画のFPSを取得
        ret, frame = self.movie.read()
        if ret==False:
            return frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return frame
        return frame
        
if __name__ == "__main__":
    camera = Camera()
    while True:
        frame = camera.get_img()
        cv2.imshow('camera', frame)
