import serial
import json
import sys

# File I/O
port_name = ""

if len(sys.argv) == 1:
    # default file
    filename = "data.json"
elif len(sys.argv) == 2:
    # input file
    filename = sys.argv[1]
elif len(sys.argv) == 3:
    # arg 3 as port_name but it is optional
    filename = sys.argv[1]
    port_name = sys.argv[2]
else:
    print("ERROR: INCORRECT INPUT. python3 pySend.py [input_file.json (optional)]")
    exit()


with open(filename) as input_file:
    try:
        data = json.load(input_file)
    except:
        print("Error opening file: ", input_file)
        exit()
# Convert File from file to string, add \n to signal end
packet = json.dumps(data) + "\n"

ser = serial.Serial(port_name)  # open serial port
ser.baudrate = 57600
ser.flush()
print(ser.name)  # check which port was really used
print(type(packet))
s = ser.write(packet.encode())  # write a string
print(packet)
print("Size, ", s)
ser.close()
