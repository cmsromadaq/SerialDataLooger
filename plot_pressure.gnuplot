set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d/%m %H:%M"
set format y "%3.1E"
set termoption dash
set yrange [1E-7:1]
set terminal png
set grid
set logscale y

set xtics 21600

#Plot absolute temp
set output "/home/cmsdaq/public_html/vacuum.png"
plot "/home/cmsdaq/data/PTU/TPG361.txt" using 1:3 with p t "pressure (mBar)"

