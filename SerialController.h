#ifndef UOP_SERIAL_CONTROLLER_H
#define UOP_SERIAL_CONTROLLER_H

#include <libserialport.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

namespace uop
{

    class SerialController
    {
    public:
        SerialController(const char* port_name, int baud_rate);
        virtual ~SerialController();

        void yeet();

        int connect(const char* port_name, int baud_rate);
        int close();

        void write(const char *msg, unsigned int timeout = 1000);
        int read(char *buffer, unsigned int size, unsigned int timeout = 1000); // If not negative, ignore

    protected:
        int check(enum sp_return result);

    private:
        char* m_port_name = nullptr;
        struct sp_port *port;
    };
}

#endif