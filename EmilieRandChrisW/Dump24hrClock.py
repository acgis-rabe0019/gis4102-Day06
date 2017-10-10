#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      chris
#
# Created:     10-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for hour in range (00,24):
    for minute in range(00,51,15):
        print '{:2}:{:2}'.format(hour,minute)