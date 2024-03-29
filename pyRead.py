import serial

ser = serial.Serial('/dev/tty.usbserial-B000B7O7') #, timeout=10)
ser.baudrate = 57600
print(ser.name) 
line = ser.readline()   # read a '\n' terminated line
print(line.decode().strip())

