#include "libserialcom.h"

namespace lsc
{
    LibSerialCom::LibSerialCom(const char *port_name, unsigned int baud_rate)
    {
        port = open(port_name, O_RDWR | O_NOCTTY);
        if (port == -1)
        {
            std::cerr << "Error opening serial port" << std::endl;
            // Handle error appropriately
            return;
        }

        struct termios tty;
        memset(&tty, 0, sizeof(tty));

        if (tcgetattr(port, &tty) != 0)
        {
            std::cerr << "Error getting serial port attributes" << std::endl;
            close(port);
            // Handle error appropriately
            return;
        }

        cfsetospeed(&tty, baud_rate);
        cfsetispeed(&tty, baud_rate);

        tty.c_cflag |= (CLOCAL | CREAD);
        tty.c_cflag &= ~PARENB;
        tty.c_cflag &= ~CSTOPB;
        tty.c_cflag &= ~CSIZE;
        tty.c_cflag |= CS8;

        tcsetattr(port, TCSANOW, &tty);
    }

    LibSerialCom::~LibSerialCom()
    {
        // Nothing is nothing!
    }

    void LibSerialCom::sendData(const char *data)
    {
        if (port != -1)
        {
            write(port, data, strlen(data));
        }
    }

    std::string LibSerialCom::readData()
    {
        std::string result;
        char buffer[256] = {0};

        if (port != -1)
        {
            ssize_t bytesRead = read(port, buffer, sizeof(buffer) - 1);
            if (bytesRead > 0)
            {
                buffer[bytesRead] = '\0';
                result = buffer;
            }
        }

        return result;
    }
}