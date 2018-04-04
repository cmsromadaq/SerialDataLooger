#!/bin/bash

if [ -e /home/cmsdaq/data/PTU/TPG361.txt ]; then
    suffix=`date '+%Y%m%d_%H%M'`
    echo "Backup old /home/cmsdaq/data/PTU/TPG361.txt into /home/cmsdaq/data/PTU/TPG361_${suffix}.txt"
    mv /home/cmsdaq/data/PTU/TPG361.txt /home/cmsdaq/data/PTU/TPG361_${suffix}.txt
fi

python tpg361_monitor.py -d /dev/ttyUSB0 -l /home/cmsdaq/data/PTU/TPG361.txt -t 2
