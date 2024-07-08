#!/usr/bin/env python3

import serial
import json
import sys


def main() -> None:
    # File I/O
    port_name = "/dev/ttyUSB0"

    if len(sys.argv) == 2:
        # input file
        port_name = sys.argv[1]
    else:
        print("ERROR: INCORRECT INPUT. python3 pySend.py [input_file.json (optional)]")
        exit()


    with serial.Serial(port_name) as ser:  # open serial port
        ser.baudrate = 57600
        ser.flush()
        while True:
            try:
                packet = sys.stdin.readline()
                s = ser.write(packet.encode())  # write a string
            except EOFError:
                break
if __name__ == "__main__":
    main()
