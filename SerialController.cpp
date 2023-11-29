#include "SerialController.h"

namespace uop
{
	SerialController::SerialController(const char* port_name, int baud_rate)
	{
		m_port_name = new char[strlen(port_name) + 1];
		strcpy(m_port_name, port_name);

		// Looking for port
		check(sp_get_port_by_name(m_port_name, &port));
		
		// Open port
		check(sp_open(port, SP_MODE_READ_WRITE));
		
		// Setting port to baud_rate 8N1, no flow control
		check(sp_set_baudrate(port, baud_rate));
		check(sp_set_bits(port, 8));
		check(sp_set_parity(port, SP_PARITY_NONE));
		check(sp_set_stopbits(port, 1));
		check(sp_set_flowcontrol(port, SP_FLOWCONTROL_NONE));
	}

	SerialController::~SerialController()
	{
		yeet();
	}

	int SerialController::connect(const char* port_name, int baud_rate)
	{
		m_port_name = new char[strlen(port_name) + 1];
		strcpy(m_port_name, port_name);

		// Config Port
		struct sp_port *port = nullptr;

		// Looking for port
		check(sp_get_port_by_name(m_port_name, &port));
		
		// Open port
		check(sp_open(port, SP_MODE_READ_WRITE));
		
		// Setting port to baud_rate 8N1, no flow control
		check(sp_set_baudrate(port, baud_rate));
		check(sp_set_bits(port, 8));
		check(sp_set_parity(port, SP_PARITY_NONE));
		check(sp_set_stopbits(port, 1));
		check(sp_set_flowcontrol(port, SP_FLOWCONTROL_NONE));

		return 0;
	}

	int SerialController::close()
	{
		check(sp_close(port));
		sp_free_port(port);

		return 0;
	}

	void SerialController::yeet()
	{
		if(m_port_name != nullptr)
		{
			delete[] m_port_name;
			m_port_name = nullptr;
		}

		if(port != nullptr)
		{
			close();
		}
	}

	void SerialController::write(const char* msg, unsigned int timeout)
	{
		int result = check(sp_blocking_write(port, msg, strlen(msg), timeout));
		if (result != strlen(msg))
			throw;
	}

	int SerialController::read(char* buffer, unsigned int size, unsigned int timeout)
	{
		int result = check(sp_blocking_read(port, buffer, size, timeout));
		buffer[result] = '\0'; // Just for safety
		return result;
	}

	int SerialController::check(enum sp_return result)
	{
		/* For this example we'll just exit on any error by calling abort(). */
		char *error_message;
		switch (result)
		{
		case SP_ERR_ARG:
			printf("Error: Invalid argument.\n");
			abort();
		case SP_ERR_FAIL:
			error_message = sp_last_error_message();
			printf("Error: Failed: %s\n", error_message);
			sp_free_error_message(error_message);
			abort();
		case SP_ERR_SUPP:
			printf("Error: Not supported.\n");
			abort();
		case SP_ERR_MEM:
			printf("Error: Couldn't allocate memory.\n");
			abort();
		case SP_OK:
		default:
			return result;
		}
	}
}