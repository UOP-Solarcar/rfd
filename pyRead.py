import serial
import json 
from datetime import datetime as dt
import sys

port_name = ''

# File I/O
if(len(sys.argv) == 1):
    # default file
    filename = "data.json"
elif(len(sys.argv) == 2):
    # input file
    filename = sys.argv[1]
elif(len(sys.argv) == 3):
    # arg 3 as port_name but it is optional
    filename = sys.argv[1]
    port_name = sys.argv[2]
else:
    print("ERROR: INCORRECT INPUT. python3 pySend.py [input_file.json (optional)] [port (optional)]")
    exit()

with serial.Serial(port_name, timeout=10) as ser:
    ser.baudrate = 57600
    print(ser.name) 
    out = ser.readline().decode().strip()   # read a '\n' terminated line
print("Received: ", out)

outfile = json.loads(out)   # convert JSON string to PYTHON dictionary so we can modified it.
# MODIFIED: ...
outfile = json.dumps(out)   # convert it back to JSON string bc write() only accept string
# serialize it into a format that can be written as a string

filename = dt.now().strftime("%d_%m_%Y %H_%M_%S")+".json" #change : and / to _
with open("testout.json", 'w') as output_file:
    output_file.write(outfile)
    # for p in line:
    #     print(p)

