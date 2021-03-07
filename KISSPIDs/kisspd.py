#!/usr/bin/env python

# KISS P/D ratio calculator
# Input P value for  Pitch axis
# Output suggested P,D values for Pitch and Roll axis

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p','--pitchp', help="Pitch P value", required=True, type=float, dest='p')
parser.add_argument('-rp','--rpdiff', help="R/P percentage difference", required=False, type=float, default=0.15, dest='rp')

args = parser.parse_args()
pitchp = float(args.p)
rpdiff = float(args.rp)

pitchd_tmp = ((10*pitchp) / 2)
pitchd = pitchd_tmp - (pitchd_tmp*0.3)

rollp = pitchp - (pitchp * rpdiff)
rolld = pitchd - (pitchd * rpdiff)

print("Starting PIDs based on Pitch P value of " + str(pitchp) +"\n")
print("Roll : P(" + str(rollp) + ") D(" + str(rolld) + ")\n")
print("Pitch: P(" + str(pitchp) + ") D(" + str(pitchd) + ")\n")

