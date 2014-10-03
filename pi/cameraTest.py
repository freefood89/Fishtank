import requests
import os
import time

for x in range(1,100):
    try:
        os.system('raspistill -w 640 -h 480 -n -q 20 -e jpg -th none -o cam.jpg')
    except:
        print('failed to capture and store image')

    try:
        with open('cam.jpg','rb') as picture:
            r = requests.post('http://192.168.1.6/uploadImage',data=picture)
    except:
        print('upload failed')
    else:
        print('file uploaded')

        
