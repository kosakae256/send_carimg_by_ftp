# 画像をftpで送信
import paramiko
import configparser
import os
import cv2
import datetime
import random
import traceback

filepath = os.path.dirname(os.path.abspath(__file__))
config_ini = configparser.ConfigParser()
config_ini.read(f'{filepath}/../config.ini', encoding='utf-8')
FTP_ID = config_ini['FTP']['FTP_ID']

def save_img(exist_img_list, indexes):
    try:

        r = random.randint(0,999999999999)
        openfile = open(f"{filepath}/../tmp/{r}", "w")
        openfile.write("")
        
        print(indexes)
        for i, img_index in enumerate(indexes):
            dt_now = datetime.datetime.now()
            filename = dt_now.strftime(f"place{FTP_ID}_{r}_{i}_%Y_%m_%d_%H_%M_%S.jpg")
            cv2.imwrite(f"{filepath}/../tmp/{filename}", exist_img_list[img_index])
        

    except:
        print(traceback.format_exc())


if __name__ == "__main__":
    im = cv2.imread("C:/Users/kosakae256/Documents/01Develop/2021yosokuru-jetson/secret/test.png")
    data_send = DataSendToFTP()
    # テストするときはcv2形式の画像を投げる
    data_send.send(im)
