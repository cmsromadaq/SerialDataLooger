import serial
import time
import logging
import os

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-d","--dev")
parser.add_option("-l","--log")
parser.add_option("-t","--time")
(options,args)=parser.parse_args()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',filename=options.log,level=logging.DEBUG)

port = options.dev
timeInterval=int(options.time) #options.time 0=100ms,1=1s,2=1m

try:
    ser = serial.Serial(port, 115200)
    ser.timeout = 5
except serial.serialutil.SerialException:
            #no serial connection
    logging.warning('not possible to establish connection with '+port)
    self.ser = None
else:
    logging.info('Starting connection with '+port)

x = ser.write('COM,%d\r\n'%timeInterval) 
alertCounter=99999
while True:
#    time.sleep(10)
#    for c in commands.keys():
#        x = ser.write(c+'\r\n')
    out = ''
        # let's wait one second before reading output (let's give device time to answer)
        #time.sleep(1)
#    while ser.inWaiting() > 0:
    out += ser.readline()
    alertCounter=alertCounter+1

    if out != '':
        if (len(out.rstrip().lstrip('0,'))!=11):
            continue
        logging.info(out.rstrip().lstrip('0,'))
        if float(out.rstrip().lstrip('0,'))>1E-3 and alertCounter>4800:
            print "SEND ALARM!"
            os.system("echo \"PRESSURE @ "+out.rstrip().lstrip('0,')+"\" | mutt -s \"ALERT FROM TPG361\" paolo.meridiani@roma1.infn.it")
            os.system("echo \"PRESSURE @ "+out.rstrip().lstrip('0,')+"\" | mutt -s \"ALERT FROM TPG361\" francesco.santanastasio@roma1.infn.it")
            os.system("echo \"PRESSURE @ "+out.rstrip().lstrip('0,')+"\" | mutt -s \"ALERT FROM TPG361\" badder.marzocchi@cern.ch")
            alertCounter=0 #send email once every 8h if problem persist

ser.close()
