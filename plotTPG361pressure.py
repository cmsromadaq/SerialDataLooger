import math
import string
import ROOT
import csv
import sys
from array import *
import re

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i","--input")
parser.add_option("-o","--output")
(options,args)=parser.parse_args()

## Inputs
#f = open("/tmp/TPG361.log", "r")
f = open(options.input, "r")
title = "pressure"

## Read data
list_steps = []
list_values = []

lines = f.readlines()
print lines
counter = -1
for line in lines:
    line = line.rstrip('\n')
    line = line.rstrip('\r')
    splittedline = line.split(' ')
    if (len(splittedline) == 3):
        try:
            float(splittedline[2])
        except:
            continue
        counter = counter+1        
        #Set start date
        if(counter == 0):
            startDate = splittedline[0]
            startTime = splittedline[1]
            print "Start date: " , startDate
            print "Start time: " , startTime
        #Fill lists
        splitteddate = splittedline[0].split('-')
        splittedtime = splittedline[1].split(':')
        #print splitteddate
        #print splittedtime        
        datetime = ROOT.TDatime(int(splitteddate[0]),int(splitteddate[1]),int(splitteddate[2]),int(splittedtime[0]),int(splittedtime[1]),int(splittedtime[2]))
        timevalue = datetime.Convert()
        #list_steps.append(float(counter))
        #print timevalue
        list_steps.append(float(timevalue))
        #splittedline[2] = re.sub('[+]', '', splittedline[2])
        #splittedline[2] = re.sub('[E]', 'e', splittedline[2])
        #print line
        #print counter
        #print float(splittedline[2])
        list_values.append(float(splittedline[2]))

Ntot = counter + 1
array_steps = array('f',list_steps)
array_values = array('f',list_values)

## Book Canvas
c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()

## Graph
g_P = ROOT.TGraph(Ntot,array_steps,array_values)
g_P.SetTitle(title)
g_P.SetLineColor(2)
g_P.SetMarkerColor(1)
g_P.SetMarkerStyle(20)

g_P.GetXaxis().SetTimeDisplay(1);
#g_P.GetXaxis().SetTimeFormat("%Y-%m-%d %H:%M");
g_P.GetXaxis().SetTimeFormat("%m-%d %H:%M");
g_P.GetXaxis().SetTimeOffset(0,"local");
g_P.GetXaxis().LabelsOption("v");
g_P.GetXaxis().SetLabelSize(0.015);
g_P.GetXaxis().SetNdivisions(510);
g_P.GetXaxis().SetTitle("Time")
g_P.GetXaxis().SetTitleOffset(1.2)
#g_P.GetXaxis().SetLimits(1464375600,1464591600)

g_P.GetYaxis().SetTitle("Pressure (mBar)")
g_P.GetYaxis().SetTitleOffset(1.3)
#print array_values[0]
#print array_values[Ntot-1]
#g_P.GetYaxis().SetRangeUser(array_values[Ntot-1]*0.1,array_values[0]*10)
g_P.GetYaxis().SetRangeUser(1e-6,10)

## Set time on xaxis
             
## Draw graph
c1.cd()
c1.SetLogy()

g_P.Draw("ap")
#h_data_MATBASE.GetYaxis().SetRangeUser(0,ROOT.TMath.Max(h_exp_MATBASE.GetMaximum()*1.1,h_data_MATBASE.GetMaximum()*1.1))
ROOT.gPad.Update()

## Legend
#legend_MATBASE = ROOT.TLegend(0.441275,0.493892,0.876,0.663176)
#legend_MATBASE.SetTextFont(72)
#legend_MATBASE.SetTextSize(0.03)
#legend_MATBASE.AddEntry(h_data_MATBASE,"Data MATBASE","lpe")
#legend_MATBASE.AddEntry(h_exp_MATBASE,"#splitline{Random Choice}{(Binomial, N=25, p=0.25)}","l")
#legend_MATBASE.Draw()

## Save Plots
c1.SaveAs(options.output+".png")
c1.SaveAs(options.output+".root")

