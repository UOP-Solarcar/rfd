import serial
import json 
from datetime import datetime as dt
import sys
# File I/O
with serial.Serial('COM12', timeout=10) as ser:
    ser.baudrate = 57600
    print(ser.name) 
    out = ser.readline().decode().strip()   # read a '\n' terminated line
print("Received: ", out)
outfile = json.loads(out)
filename = dt.now().strftime("%d/%m/%Y %H:%M:%S")+".json"
with open("testout.json", 'w') as output_file:
    output_file.write(outfile)
    # for p in line:
    #     print(p)

