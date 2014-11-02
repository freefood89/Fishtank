import serial

print("Sensor Demo")

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 38400)

ser.write(bytes("L1\r",'UTF-8'))
ser.write(bytes("C\r",'UTF-8'))

line=""

while True:
    data = ser.read().decode('UTF-8')
    if(data == "\r"):
        print("Received:", line)
	line=""
    else:
	line = line + data
		
