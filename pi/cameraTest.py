import requests
import os
import time
import picamera

for x in range(1,100):
    with picamera.PiCamera() as camera:
        camera.resolution=(640,480)
        camera.capture('image.jpg')

    try:
        with open('image.jpg','rb') as picture:
            r = requests.post('http://renomania.ddns.net/uploadImage',data=picture)
    except:
        print('upload failed')
    else:
        print('file uploaded')
    t1 = time.time()
    while time.time()-t1<10:
        pass

        
