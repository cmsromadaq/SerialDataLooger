import serial
import time

port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600)
ser.timeout = 5
commands = {} 
commands['IN_PV_00']='TBATH='
commands['STATUS']='STAT='

while True:
    time.sleep(5)
    for c in commands.keys():
        x = ser.write(c+'\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print commands[c]+out.rstrip().lstrip(' ')

ser.close()
