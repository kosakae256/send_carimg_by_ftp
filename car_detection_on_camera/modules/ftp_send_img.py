# 画像をftpで送信
import paramiko
import configparser
import os
import cv2
import datetime

filepath = os.path.dirname(os.path.abspath(__file__))

config_ini = configparser.ConfigParser()
config_ini.read(f'{filepath}/../config.ini', encoding='utf-8')

# 定数定義
HOSTNAME = config_ini['FTP']['HOSTNAME']
PORT = int(config_ini['FTP']['PORT'])
USERNAME = config_ini['FTP']['USERNAME']
PRIVATE_KEY = config_ini['FTP']['PRIVATE_KEY']
PASSPHRASE = config_ini['FTP']['PASSPHRASE']
FTP_ID = config_ini['FTP']['FTP_ID']

class DataSendToFTP():
    def __init__(self):
        # 接続準備
        self.login()


    def login(self):
        self.transport = paramiko.Transport((HOSTNAME, PORT))
        rsa_private_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY,PASSPHRASE)
        self.transport.connect(username=USERNAME, pkey= rsa_private_key)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)


    def send(self,exist_img):
        dt_now = datetime.datetime.now()
        filename = dt_now.strftime(f"place{FTP_ID}_%Y_%m_%d_%H_%M_%S.jpg")
        cv2.imwrite(filepath + "/../tmp/" + filename,exist_img)
        self.sftp.put(filepath + "/../tmp/" + filename, f"receive_imgs/place{FTP_ID}/" + filename)
        self.login()
        

if __name__ == "__main__":
    im = cv2.imread("C:/Users/kosakae256/Documents/01Develop/2021yosokuru-jetson/secret/test.png")
    data_send = DataSendToFTP()
    # テストするときはcv2形式の画像を投げる
    data_send.send(im)
