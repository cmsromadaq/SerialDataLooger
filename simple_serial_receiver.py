import serial
from time import sleep

port = "/dev/ttyACM2"
ser = serial.Serial(port, 9600, timeout=0)

while True:
    data = ser.read(9999)
    if len(data) > 0:
        print 'Got:', data.rstrip()
        
    sleep(0.1)
#    print 'not blocked'

ser.close()
