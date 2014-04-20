#!/usr/bin/python

import MySQLdb
from serial_monitor import SerialData as DataGen
from time import sleep

#establish connection to MySQL. You'll have to change this for your database.
dbConn = MySQLdb.connect("localhost","database_username","password","database_name") or die ("could not connect to database")
#open a cursor to the database
cursor = dbConn.cursor()

device = '/tmp/COM0' #this will have to be changed to the serial port you are using
try:
      print "Trying...",device
      serial = DataGen(device, 9600)
except:
      print "Failed to connect on",device

while True: #the infinite loop
    sleep(1)
    try:
        data = serial.next()  #read the data from the arduino (lines are split by \n)
        pieces = data.split(" ")  #split the data by the tab
        if len(pieces)<2:
              continue
        else:
              sensor=pieces[0]
              measurements={}
              for meas in pieces[1:]:
                    meas_type=meas.split("=")[0]
                    meas_value=meas.split("=")[0]
                    measurements[sensor+'_'+meas_type]=meas_value
    #Here we are going to insert the data into the Database
        try:
            cursor.execute("INSERT INTO weatherData (humidity,tempC) VALUES (%s,%s)", (pieces[0],pieces[1]))
            dbConn.commit() #commit the insert
            cursor.close()  #close the cursor
        except MySQLdb.IntegrityError:
            print "failed to insert data"
        finally:
            cursor.close()  #close just incase it failed
    except:
        print "Failed to get data from serial"
