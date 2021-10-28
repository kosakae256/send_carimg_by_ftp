#!/usr/bin/python3.6
# 画像をftpで送信
import paramiko
import configparser
import os
import datetime
import random
import traceback
from time import sleep
import glob


filepath = os.path.dirname(os.path.abspath(__file__))

config_ini = configparser.ConfigParser()
config_ini.read(f'{filepath}/config.ini', encoding='utf-8')

# 定数定義
HOSTNAME = config_ini['FTP']['HOSTNAME']
PORT = int(config_ini['FTP']['PORT'])
USERNAME = config_ini['FTP']['USERNAME']
PRIVATE_KEY = config_ini['FTP']['PRIVATE_KEY']
PASSPHRASE = config_ini['FTP']['PASSPHRASE']
FTP_ID = config_ini['FTP']['FTP_ID']
transport = paramiko.Transport((HOSTNAME, PORT))
rsa_private_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY,PASSPHRASE)
transport.connect(username=USERNAME, pkey= rsa_private_key)
sftp = paramiko.SFTPClient.from_transport(transport)

def send():
    try:
        # img send after id send
        file_list = glob.glob(f"{filepath}/tmp/*.jpg")
        sleep(10)
        for f in file_list:
            filename = os.path.basename(f)
            print(filename)
            sftp.put(f, f"yosokuru/imgs/place{FTP_ID}/{filename}")
            os.remove(f)

        file_list = glob.glob(f"{filepath}/tmp/*")
        for f in file_list:
            filename = os.path.basename(f)
            sftp.put(f, f"yosokuru/ids/place{FTP_ID}/{filename}")
            os.remove(f)

    except:
        sleep(30)
        os.system("reboot")
        


if __name__ == "__main__":
    while True:
        send()
        sleep(60*1)
        
            
