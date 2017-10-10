#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mie_r
#
# Created:     10-10-2017
# Copyright:   (c) mie_r 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x=0
while x<= 4:
    x += 1
    if x == 2: continue
    print x
else:
    print "Loop done."


for i in [1,2,3,4]:
    if i == 2: continue
    if i == 3: break
    print i
else:
    print "Loop done."

