import serial

print("Sensor Demo")

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 38400)

ser.write("L1\r")
ser.write("C\r")

line=""

while True:
	data = ser.read()
	if(data == "\r"):
		print("Received:", line)
		line=""
	else:
		line = line + data
		
