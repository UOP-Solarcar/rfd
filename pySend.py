import serial
ser = serial.Serial('/dev/tty.usbserial-B000B7O7')  # open serial port
ser.baudrate = 57600
ser.flush()
print(ser.name)         # check which port was really used
packet = 'test now\n'
print(type(packet))
s = ser.write(packet.encode())     # write a string
print(packet)
print("Size, ", s)
ser.close()  

