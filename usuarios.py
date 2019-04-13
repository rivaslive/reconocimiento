import serial, time


def reconocido():
    arduino = serial.Serial("COM8", 9600)
    time.sleep(2)
    arduino.write(b'1')
    arduino.close()

def desconocido():
    arduino = serial.Serial("COM8", 9600)
    time.sleep(2)
    arduino.write(b'2')
    arduino.close()


#ejecuta la accion de encender el LED pin 11
reconocido()
time.sleep(3)

#APAGA el led del pin 11 y enciende el del pin 8
desconocido()

