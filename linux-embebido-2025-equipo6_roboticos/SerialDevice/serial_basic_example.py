import time 
# 3er party libreries (like pyserial)
import serial
# lastly local modules


SERIAL_PORT= 'COM9'
BAUDRATE= 9600
serial_device = serial.Serial(
    port = SERIAL_PORT,
    baudrate = BAUDRATE
)

time.sleep(2)
serial_device.write(b"Connect")
message = serial_device.readline()

#pregunta: que tipo de dato es message?
print(type(message))
print(message.decode(encoding = 'utf-8'))

while True:
    try:
        to_send = input ('Mensaje a enviar: ')
        serial_device.write(to_send.encode())
        time.sleep(1)
        received = serial_device.readline()
        print(received.decode())
    except KeyboardInterrupt:
        break
serial_device.close()