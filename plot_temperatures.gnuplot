set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M"
set termoption dash
set yrange [18:27]
set terminal png
set output "/tmp/temperatures.png"
plot "/tmp/temperatures" using 1:3 w l lt 1 lc rgb "green" lw 3 t "SHT75",  "/tmp/temperatures" using 1:4 w l lt 1 lc rgb "blue" lw 3 t "LM35_1", "/tmp/temperatures" using 1:5 w l lt 1 lc rgb "red" lw 3 t "LM35_2"
set output "/tmp/temperatures_diff.png"
set yrange [-2:2]
plot "/tmp/temperatures" using 1:($4-$3) w l lt 1 lc rgb "green" lw 3 t "LM35_1-SHT75",  "/tmp/temperatures" using 1:($5-$3) w l lt 1 lc rgb "blue" lw 3 t "LM35_2-SHT75"
