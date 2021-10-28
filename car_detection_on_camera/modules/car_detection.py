# 車検出モデルを動かす
from efficientnet_pytorch import EfficientNet
import torch
import torch.nn as nn
import glob
import torchvision.transforms as transforms
import cv2
import numpy as np
import os
from PIL import Image

torch.backends.cudnn.banchmark = True
filepath = os.path.dirname(os.path.abspath(__file__))

class CarDetection():
    def __init__(self):
        self.labels = ["exist","nothing"]
        model_path = f"{filepath}/../models/exist_or_nothing_v3.pth"
        self.device = torch.device("cuda")

        print(self.device)

        self.model = EfficientNet.from_pretrained("efficientnet-b0")
        num_ftrs = self.model._fc.in_features
        self.model._fc = nn.Linear(num_ftrs, 2)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        self.model.cuda()
        self.model = self.model.to(self.device,non_blocking=True)

        self.transform = transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor()])

    def detect(self,img_from_camera):
        x = Image.fromarray(img_from_camera)
        x = self.transform(x)
        data = x.to(self.device, non_blocking=True).unsqueeze(0)
        output = self.model(data)
        c = int(output.argmax())
        print(output)
        print(self.labels[c])
         
        # 車なし
        if self.labels[c] == "nothing":
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
