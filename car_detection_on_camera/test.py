from efficientnet_pytorch import EfficientNet
import torch
import torch.nn as nn
import glob
import torchvision.transforms as transforms
import cv2
import numpy as np
import os
from PIL import Image

filepath = os.path.dirname(os.path.abspath(__file__))

torch.backends.cudnn.banchmark = True

device = torch.device("cuda")

print(device)

model = EfficientNet.from_pretrained("efficientnet-b0")
num_ftrs = model._fc.in_features
model._fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load(f"{filepath}/models/exist_or_nothing_v3.pth"))
model.eval()
model.cuda()
model = model.to(device,non_blocking=True)

print("a")

transform = transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor()])
for i in range(0,100):
    x = np.zeros((224,224,3),dtype=np.uint8)
    x = Image.fromarray(x)
    x = transform(x)
    data = x.to(device, non_blocking=True).unsqueeze(0)
    print("classification start")
    output = model(data)
    c = int(output.argmax())
    print(c)
    print(i)

