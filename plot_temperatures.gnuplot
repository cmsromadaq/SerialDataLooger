set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d@%H"
set termoption dash
set yrange [18:27]
set terminal png

#Plot absolute temp
set output "/var/www/TEMP/temperatures.png"
plot ["2014-04-28 15:00:00":] "/tmp/temperatures" using 1:3 with p t "SHT75 CeF3", "/tmp/temperatures" using 1:4 w p t "LM35_1 BGO Front", "/tmp/temperatures" using 1:5 w p t "LM35_2 BGO Back"

#Plot relative differences
set output "/var/www/TEMP/temperatures_diff.png"
set yrange [-3:3]
plot ["2014-04-28 15:00:00":] "/tmp/temperatures" using 1:($4-$3) with p t "LM35_1-SHT75",  "/tmp/temperatures" using 1:($5-$3) with p t "LM35_2-SHT75" ,  "/tmp/temperatures" using 1:($5-$4) with p t "LM35_2-LM35_1"

#plot "/tmp/temperatures" using 1:3 w p rgb "green" t "SHT75",  "/tmp/temperatures" using 1:4 w p rgb "blue" t "LM35_1", "/tmp/temperatures" using 1:5 w p rgb "red" t "LM35_2"
#set output "/var/www/TEMP/temperatures_diff.png"
#
#plot "/tmp/temperatures" using 1:($4-$3) w l lt 1 lc rgb "green" lw 3 t "LM35_1-SHT75",  "/tmp/temperatures" using 1:($5-$3) w l lt 1 lc rgb "blue" lw 3 t "LM35_2-SHT75"
