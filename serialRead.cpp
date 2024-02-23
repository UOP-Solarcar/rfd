#include "lib/serialib.h"
static const char* PORT = "/dev/ttyUSB1";
serialib serial;

int main(){
    char errorOpening = serial.openDevice(PORT, 115200);
    // If connection fails, return the error code otherwise, display a success message
    if (errorOpening!=1) return errorOpening;
    printf ("Successful connection to %s\n",PORT);
    char buffer[8];
    serial.readBytes(buffer, 8, 20000, 1000);     
for (int i=0; i<8 ; i++)
    printf("Receive [%d] = %d\n", i, buffer[i]);
    serial.closeDevice();
    return 0;
}