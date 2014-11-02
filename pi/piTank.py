import picamera
import RPIO
import time
import requests
import json
import signal
import sys

LEDMap = {'led1':17}
RPIOMap = {'On': True, 'Off': False}

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        if input('¥nReally quit? (y/n)>').lower().startswith('y'):
            print('Cleaning Up RPIO')
            RPIO.cleanup()
            sys.exit(1)
    except KeyboardInterrupt:
        print('quitting')
        sys.exit(1)

def update_LEDs(state):
    for key in state:
        if key not in LEDMap or state[key] not in RPIOMap:
            #print('could not map')
            break
        #print(key,state[key])
        #print(LEDMap[key],RPIOMap[state[key]])
        RPIO.output(LEDMap[key], RPIOMap[state[key]])

def init_LEDs():
    for led in LEDMap:
        RPIO.setup(LEDMap[led], RPIO.OUT, initial=RPIO.LOW)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    init_LEDs()
    while True:
        t1 = time.time()
        try:
            r = requests.get('http://renomania.ddns.net/~/state')
            leds = json.loads(r.text)
        except Exception as e:
            print(e)
        else:
            #print('Updating LEDs')
            update_LEDs(leds)
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
        
        while time.time() - t1 < 3:
            pass
