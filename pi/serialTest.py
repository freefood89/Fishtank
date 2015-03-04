import serial

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
if not ser.isOpen():
	print('opening serial port')
	ser.open()

while True:
	s = input('<')
	ser.write((s+'\n').encode());
	print(ser.readline().strip().decode('utf-8'))
	# print('.')

ser.close()
