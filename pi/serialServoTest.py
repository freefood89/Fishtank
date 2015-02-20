import serial

ser = serial.Serial('/dev/tty.usbmodem1441', 9600)
if not ser.isOpen():
	print('opening serial port')
	ser.open()

for i in range(10):
	serialOut = input('<')
	ser.write((serialOut+'\n').encode())
	print('>'+ser.readline().strip().decode('utf-8'))
	# print('.')

ser.close()