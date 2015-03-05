import serial
import time

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
if not ser.isOpen():
	print('opening serial port')
	ser.open()
print('Waiting to Connect')
time.sleep(3)
print('starting')
while True:
	s = input('<')
	# ser.write(b'test')
	print(ser.readline().strip().decode('utf-8'))
	# print('.')

ser.close()
