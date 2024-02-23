#include "lib/serialib.h"
static const char* PORT = "/dev/ttyUSB0";
serialib serial;

int main(){
    char errorOpening = serial.openDevice(PORT, 115200);
    // If connection fails, return the error code otherwise, display a success message
    if (errorOpening!=1) return errorOpening;
    unsigned char buffer[8] = {1, 3, 5, 7, 11, 13, 17, 19};
    serial.writeBytes(buffer, 8); 

    serial.closeDevice();
    return 0;
}