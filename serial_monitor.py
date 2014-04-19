"""
Listen to serial, return most recent numeric values
Lots of help from here:
http://stackoverflow.com/questions/1093598/pyserial-how-to-read-last-line-sent-from-serial-device
"""
from threading import Thread
import time
import serial

last_received = ''
def receiving(ser):
    global last_received
    buffer = ''
    while True:
        if '\n' in buffer:
            last_received, buffer = buffer.split('\n')[-2:]
#            print "lastline "+last_received+" BUFFER "+buffer
        else:
            buffer += ser.read(9999)  # this will block until one more char or timeout
        buffer += ser.read(ser.inWaiting()) # get remaining buffered chars


class SerialData(object):
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, init=50):
        try:
            self.ser = ser = serial.Serial(
                port,
                baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
                )
        except serial.serialutil.SerialException:
            #no serial connection
            print 'not possible to establish connection with '+port
            self.ser = None
        else:
            print 'Starting connection with '+port
            Thread(target=receiving, args=(self.ser,)).start()

    def next(self):
        global last_received
        if self.ser == None:
            return -9999 #return anything so we can test when Arduino isn't connected
        #return a float value or try a few times until we get one
        while True:
            raw_line = last_received
            if raw_line == '':
                time.sleep(.005)
                continue
            try:
                last_received=''
                print "Got data: "+raw_line.strip()
                return raw_line.strip()
            except ValueError:
                continue
        return 0.

    def __del__(self):
        if self.ser:
            self.ser.close()
            
            

if __name__=='__main__':
    port='/tmp/COM0'
    s = SerialData(port)
    while True:
        data=s.next()
        if data==-9999:
            print 'no connection with '+port+". Quit"
            exit(-1)

