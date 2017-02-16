set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d/%m %H:%M"
set format y "%3.1E"
set termoption dash
set yrange [10:30]
set terminal png
set grid

set xtics 21600

#Plot absolute temp
set output "/home/cmsdaq/public_html/temp.png"
plot "<sed -e 's%T1=%%g' /home/cmsdaq/data/PTU/temp.txt" using 1:3 with p t "temp"

#Plot relative differences
#set output "/var/www/TEMP/temperatures_diff.png"
#set yrange [-6:3]
#plot ["2014-05-19 10:00:00":] "/tmp/temperatures" using 1:($4-$3) with p t "LM35_1-SHT75",  "/tmp/temperatures" using 1:($5-$3) with p t "LM35_2-SHT75" ,  "/tmp/temperatures" using 1:($5-$4) with p t "LM35_2-LM35_1"

#plot "/tmp/temperatures" using 1:3 w p rgb "green" t "SHT75",  "/tmp/temperatures" using 1:4 w p rgb "blue" t "LM35_1", "/tmp/temperatures" using 1:5 w p rgb "red" t "LM35_2"
#set output "/var/www/TEMP/temperatures_diff.png"
#
#plot "/tmp/temperatures" using 1:($4-$3) w l lt 1 lc rgb "green" lw 3 t "LM35_1-SHT75",  "/tmp/temperatures" using 1:($5-$3) w l lt 1 lc rgb "blue" lw 3 t "LM35_2-SHT75"
