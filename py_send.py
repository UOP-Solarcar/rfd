#!/usr/bin/env python3

import serial
import sys


def main() -> None:
    # File I/O
    port_name = "/dev/ttyUSB0"

    if len(sys.argv) == 2:
        # input file
        port_name = sys.argv[1]

    with serial.Serial(port_name) as ser:  # open serial port
        ser.baudrate = 57600
        ser.flush()
        while True:
            try:
                s = ser.write(sys.stdin.buffer.readline())  # write a string
            except EOFError:
                break


if __name__ == "__main__":
    main()
