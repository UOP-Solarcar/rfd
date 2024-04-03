import serial
import json
import sys

# File I/O
if(len(sys.argv) == 1):
    # default file
    filename = "data.json"
elif(len(sys.argv) == 2):
    # input file
    filename = sys.argv[1]
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
packet = json.dumps(data) + '\n'

ser = serial.Serial('COM10')  # open serial port
ser.baudrate = 57600
ser.flush() 
print(ser.name)         # check which port was really used
print(type(packet))
s = ser.write(packet.encode())     # write a string
print(packet)
print("Size, ", s)
ser.close()  

