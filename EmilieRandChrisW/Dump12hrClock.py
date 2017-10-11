#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mie_r
#
# Created:     10-10-2017
# Copyright:   (c) mie_r 2017
# Licence:     <your licence>
#------------------------------------------------------------------------------
for hour in range (00,12):
        for minute in range (00,51,15):
            ampm='AM'
            print '{:02}:{:02}{}'.format(hour,minute,ampm)

for hour in range (00,12):
    for minute in range (00,51,15):
        ampm='PM'
        print '{:02}:{:02}{}'.format(hour,minute,ampm)