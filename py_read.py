import serial
import json
from datetime import datetime as dt
import sys


### IMPORTANT: This is a template script. JSON deserialization logic must be revised according to CAN bus frames.

port_name = ""

# File I/O
if len(sys.argv) == 2:
    port_name = sys.argv[1]
else:
    print("ERROR: INCORRECT INPUT. python3 pyRecv.py [port]")
    exit()

try:
    with serial.Serial(port_name, baudrate=57600, timeout=10) as ser:
        print(f"Using port: {ser.name}")  # check which port was really used

        while True:
            out = ser.readline().decode().strip()  # read a '\n' terminated line
            if out:
                print("Received: ", out)

                try:
                    # Convert JSON string to PYTHON dictionary
                    received_data = json.loads(out)

                    # Process or modify the received_data if necessary
                    # MODIFIED: ...

                    # Convert it back to JSON string bc write() only accepts string
                    outfile = json.dumps(received_data, indent=4)

                    # Create a timestamped filename
                    timestamped_filename = dt.now().strftime("%d_%m_%Y_%H_%M_%S") + ".json"

                    # Write the JSON data to a file
                    with open(timestamped_filename, "w") as output_file:
                        output_file.write(outfile)

                    print(f"Data saved to {timestamped_filename}")
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")

except serial.SerialException as e:
    print(f"Serial exception: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
