#ifndef LSC_LIB_SERIAL_COM_H
#define LSC_LIB_SERIAL_COM_H

#include "pch.h"

namespace lsc
{
    class LibSerialCom
    {
    public:
        // port_name, baud_rate
        LibSerialCom(const char*, unsigned int);
        
        ~LibSerialCom();

        void sendData(const char* data);

        std::string readData();

    private:
        int port = 0;
    };
}

#endif