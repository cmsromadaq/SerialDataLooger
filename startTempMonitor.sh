#!/bin/bash                                                                                                                    

if [ -e /home/cmsdaq/data/PTU/temp.txt ]; then
    suffix=`date '+%Y%m%d_%H%M'`
    echo "Backup old /home/cmsdaq/data/PTU/temp.txt into /home/cmsdaq/data/PTU/temp_${suffix}.txt"
    mv /home/cmsdaq/data/PTU/temp.txt /home/cmsdaq/data/PTU/temp_${suffix}.txt
fi

python logTemperatures.py -d /dev/ttyACM0 -n 3 -l /home/cmsdaq/data/PTU/temp.txt
