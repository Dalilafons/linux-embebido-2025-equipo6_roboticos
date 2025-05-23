import sys
import time
import os
import serial 


BAUDRATES = [
    4800, 
    9600,
    38400,
    460800,
    57600,
    115200,
    230400
]

class SerialDevice:
    def _init_(self, port:str, baudrate:int):
        if baudrate not in BAUDRATES:
            raise ValueError(f"Not a valid baudrate {baudrate}")
        if port not in self.find_available_serial_port():
            raise ValueError(f'Not a valid port {port}')

        self.serial_device = serial.Serial(
            port = port,
            baudrate = baudrate
        )
        time.sleep(2)
        self.serial_device.write(b'Connect')
        time.sleep(1)
        m = self.serial_device.readline()
        print(m.decode())
        m = self.serial_device.readline()
        print(m.decode())
        
    def send_message(self, message:str)->str:
        self.serial_device(message.encode())
        time.sleep(1)
        return self.read_message()
    

    def read_message(self)->str:
        return self.serial_device.readline().decode()
    
    def disconected(self)->None:
        self.serial_device.close()
    
    @staticmethod
    def find_available_serial_port()->list[str]:
        if sys.platform.startswith('darwin'):
            ports = os.listdir('/dev/')
            ports = [f'/dev/{port}' for port in ports if port.startswith('cu.')]
        elif sys.platform.startswith('linux'):
            ports = os.listdir('/dev/')
            ports = [f'/dev/{port}' for port in ports if port.startswith('ttyA')]
        elif sys.platform.startswith('win'):
            ports = [f'COM{i}' for i in range(1, 256)]

            
        else:
            return []
        return ports