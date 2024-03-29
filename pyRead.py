import serial

with serial.Serial('COM12', 57600, timeout=10) as ser:
    print(ser.name) 
    line = ser.read(7)   # read a '\n' terminated line
    print(line)

