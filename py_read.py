#!/usr/bin/env python3

import serial
from datetime import datetime as dt
import sys


def main() -> None:
    port_name = "/dev/ttyUSB0"

    # File I/O
    if len(sys.argv) == 2:
        # input file
        port_name = sys.argv[1]

    with serial.Serial(port_name) as ser:
        ser.baudrate = 57600
        while True:
            sys.stdout.buffer.write(ser.readline())
            sys.stdout.flush()
        #out = ser.readline().decode().strip()  # read a '\n' terminated line


if __name__ == "__main__":
    main()
