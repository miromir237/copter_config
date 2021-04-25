#!/usr/bin/env python
# (pi/4)*square(mwidth)*mheight

import argparse
import math 

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-mw','--mwidth', help="Motor width", required=True, type=float, default=23, dest='mw')
parser.add_argument('-mh','--mheight', help="Motor height", required=False, type=float, default=6, dest='mh')

args = parser.parse_args()

# Setting variables
mwidth = float(args.mw)
mheight = float(args.mh)

mvol_prop_table = {
    (0,350): "1-2",
    (350, 650): "2-3",
    (650, 1250): "3-3.5",
    (1250, 1750): "4 inch, low pitch 5",
    (2000, 3000): "5 inch, 5.1 inch, low pitch 6",
    (3000, 4100): "6 inch and light 7", 
    (4000, 6000): "7"
}

# defining functions/method
def get_prop(table, motor_volume):
    for key in table:
        if key[0] < motor_volume < key[1]:
            return table[key]

def main():
    mvolume = (math.pi/4)*math.pow(mwidth, 2)*mheight
    print("Motor volume is " + str(mvolume))  
    print("Your motor is suitable for " + str(get_prop(mvol_prop_table,mvolume)) + " inch prop.")

# Executing the program
if __name__ == "__main__":
    main()