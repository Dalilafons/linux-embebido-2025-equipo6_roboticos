import serial
import time

puerto = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

mensaje_original = ""
mensaje_cifrado = ""

while True:
    if puerto.in_waiting > 0:
        linea = puerto.readline().decode('utf-8').strip()

        if linea.startswith("MSG:"):
            mensaje_original = linea.replace("MSG:", "")
        elif linea.startswith("CIF:"):
            mensaje_cifrado = linea.replace("CIF:", "")
            print("Mensaje original:", mensaje_original)
            print("Cifrado César:", mensaje_cifrado)
            break  
