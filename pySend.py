import serial
ser = serial.Serial('COM10')  # open serial port
ser.flush()
print(ser.name)         # check which port was really used
packet = bytearray('test message', 'utf-8')
print(type(packet))
s = ser.write(packet)     # write a string
print(packet)
print("Size, ", s)
ser.close()  

