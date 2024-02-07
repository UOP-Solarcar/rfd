// #include "SerialController.h"
#include "libserialcom.h"
#include <iostream>
const char* PORT_NAME = "/dev/ttyUSB1";
const unsigned int BAUD_RATE = 96000;


int main(){
    lsc::LibSerialCom reciever(PORT_NAME, BAUD_RATE);
    std::cout << "Living";
    while(true){
        std::cout << reciever.readData();
        // std::cout << "Data Recieved";

        // std::cout << data;
    }
    
    return 0;
}