#include "CppLinuxSerial/SerialPort.hpp"

using namespace mn::CppLinuxSerial;

int main() {
	// Create serial port object and open serial port at 57600 baud, 8 data bits, no parity bit, one stop bit (8n1),
	// and no flow control
	SerialPort serialPort("/dev/ttyUSB2", BaudRate::B_57600, NumDataBits::EIGHT, Parity::NONE, NumStopBits::ONE);
	// Use SerialPort serialPort("/dev/ttyACM0", 13000); instead if you want to provide a custom baud rate
	serialPort.SetTimeout(100); // Block for up to 100ms to receive data
	serialPort.Open();

	// WARNING: If using the Arduino Uno or similar, you may want to delay here, as opening the serial port causes
	// the micro to reset!
	// while(true){	// Write some ASCII data
	serialPort.Write("AMONG US XD");

	// }
	// Close the serial port
	serialPort.Close();
}