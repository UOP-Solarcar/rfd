import serial

with serial.Serial('/dev/ttyUSB1', timeout=10) as ser:
    ser.baudrate = 57600
    print(ser.name) 
    line = ser.readline()   # read a '\n' terminated line
    print(line.decode().strip())
    # for p in line:
    #     print(p)

