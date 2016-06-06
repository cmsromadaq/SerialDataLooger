#!/bin/bash
source /home/cmsdaq/root/bin/thisroot.sh
python /home/cmsdaq/SerialDataLooger/plotTPG361pressure.py -i $1 -o $2
