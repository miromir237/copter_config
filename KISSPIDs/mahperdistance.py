#!/usr/bin/env python3

import argparse

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d','--distance', help="Expected distance", required=True, type=int, default=4, dest='d')

args = parser.parse_args()

avg_speed = 75  # average speed in km/h
mininhour = 60  # minutes in 1 hour
expect_distance = int(args.d) # expected distance in km
mah_per_min = 100   #power consumption per minute average

flight_time = (expect_distance/avg_speed)*mininhour
expect_consumption = flight_time * mah_per_min

print("Average speed:\t\t\t" + str(avg_speed) + " km/h")
print("Flight distance:\t\t" + str(expect_distance) + " km")
print("Expect flight time:\t\t" + str(flight_time) + " minutes") 
print("Expected mAh consumption:\t" + str(expect_consumption) + " mAh")
