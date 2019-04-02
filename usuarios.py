import serial, time


def reconocido():
    arduino = serial.Serial("COM3", 9600)
    time.sleep(2)
    arduino.write(b'1')
    arduino.close()

def desconocido():
    arduino = serial.Serial("COM3", 9600)
    time.sleep(2)
    arduino.write(b'2')
    arduino.close()
