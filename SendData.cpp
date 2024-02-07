// #include "SerialController.h"
#include "libserialcom.h"
#include <iostream>
const char* PORT_NAME = "/dev/ttyUSB0";
const unsigned int BAUD_RATE = 96000;


int main(){
    lsc::LibSerialCom sender(PORT_NAME, BAUD_RATE);
    std::cout << "Live";
    while(true){
        const char* str = 't';
        sender.sendData(str);
        // std::cout << "Data Sent";
    }
    
    return 0;
}