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
loopcount=0
total_iterations=96
while loopcount<total_iterations:
    loopcount+=1
    for hour in range (00,12):
        for minute in range (00,51,15):
            count=0
            if count<48:
                ampm='AM'
                count+=1
                print '{}:{}{}'.format(hour,minute,ampm)

                if ampm=='AM': continue

            else:
                ampm='PM'
                count+=1

            print '{}:{}{}'.format(hour,minute,ampm)
