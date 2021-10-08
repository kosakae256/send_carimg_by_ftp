# 車検出モデルを動かす
from keras.models import load_model
import cv2
import numpy as np
import os

filepath = os.path.dirname(os.path.abspath(__file__))

class CarDetection():
    def __init__(self):
        self.labels = ["exist","nothing"]
        model_path = f"{filepath}/../models/exist_or_nothing.h5"
        self.model = load_model(model_path)

    def detect(self,img_from_camera):
        # 299x299にreshape
        x = cv2.resize(img_from_camera,(299,299))
        # 配列に新しい次元を追加する
        x = np.expand_dims(x, axis=0)
        # 色を0~1までの値に変換
        x = x / 255

        # 推論
        result = self.model.predict(x)[0][0]
        print(result)
        # 車なし
        if result<=0.4:
            return False
        # 車あり
        else:
            return True

if __name__ == "__main__":
    car_detection = CarDetection()
    for i in range(1,9):
        img = cv2.imread(f"{filepath}/../secret/test{i}.jpg")
        # テストするときはcv2形式の画像を投げる
        j = car_detection.detect(img)
        print(j)
