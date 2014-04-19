import serial
from time import sleep

port = "/tmp/COM1"
ser = serial.Serial(port, 9600)
while True:
    x = ser.write('999.\n')
    print "OK"
    sleep(1)
ser.close()
