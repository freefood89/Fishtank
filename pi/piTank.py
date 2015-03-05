# import picamera
import time
import requests
import json
import signal
import sys
import serial

DeviceMap = {'led1':'led_1', 'led2':'led_2','servo1':'servo_1'}
OutputMap = {'On': 127, 'Off': 0, 'left':0, 'right':180}
ser = serial.Serial('/dev/ttyACM0',timeout=2,baudrate=9600)
# ser = serial.Serial('/dev/tty.usbmodem1441', 9600)
time.sleep(3)

if not ser.isOpen():
    print('opening serial port')
    ser.open()

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        if input('¥nReally quit? (y/n)>').lower().startswith('y'):
            # print('Cleaning Up RPIO')
            # RPIO.cleanup()
            sys.exit(1)
    except KeyboardInterrupt:
        print('quitting')
        sys.exit(1)

def update_Devices(state):
    for led in state:
        if led in DeviceMap and state[led] in OutputMap:
            # a = input()
            serialOut = ' '.join([DeviceMap[led], str(OutputMap[state[led]])])
            # print('led_1 127'==serialOut)
            print(serialOut)
            ser.write((serialOut+'\n').encode())
            print(ser.readline().strip().decode('utf-8'))

def log(message):
    output = message #add time stamp
    print(output)
    #add write to logger

# def init_LEDs():
#     for led in LEDMap:
#         RPIO.setup(LEDMap[led], RPIO.OUT, initial=RPIO.LOW)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    # init_LEDs()
    while True:
        t1 = time.time()
        try:
            r = requests.get('http://renomania.ddns.net/devices/~')
            devices = json.loads(r.text)
        except Exception as e:
            print(e)
        else:
            print('Updating LEDs')
            print(devices)
            update_Devices(devices)
        # with picamera.PiCamera() as camera:
        #     camera.resolution=(640,480)
        #     camera.capture('image.jpg')
        # try:
        #     with open('image.jpg','rb') as picture:
        #         r = requests.post('http://renomania.ddns.net/uploadImage',data=picture)
        # except:
        #     print('upload failed')
        # else:
        #     print('file uploaded')
        
        # while time.time() - t1 < 3:
        #     pass
