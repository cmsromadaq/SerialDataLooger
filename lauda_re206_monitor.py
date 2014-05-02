import serial
import time
import logging

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-d","--dev")
parser.add_option("-l","--log")
(options,args)=parser.parse_args()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',filename=options.log,level=logging.DEBUG)

port = options.dev

try:
    ser = serial.Serial(port, 9600)
    ser.timeout = 5
except serial.serialutil.SerialException:
            #no serial connection
    logging.warning('not possible to establish connection with '+port)
    self.ser = None
else:
    logging.info('Starting connection with '+port)

commands = {} 
commands['IN_PV_00']='TBATH='
commands['STATUS']='STAT='

while True:
    time.sleep(10)
    for c in commands.keys():
        x = ser.write(c+'\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            logging.info(commands[c]+out.rstrip().lstrip(' '))

ser.close()
