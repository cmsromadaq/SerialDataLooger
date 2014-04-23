#!/bin/sh

 awk  '/SENS1/{split($4,a,"="); temp1=a[2]} /SENS2/{split($4,a,"="); temp2=a[2]} /SENS3/{split($4,a,"="); temp3=a[2]; if(temp1>0 && temp2>0 && temp3>0) printf "%s %s %4.2f %4.2f %4.2f\n",$1,$2,temp1,temp2,temp3}' serial_monitor.log > /tmp/temperatures
gnuplot plot_temperatures.gnuplot
echo "Prepared /tmp/temperatures.png"