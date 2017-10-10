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

def main():
    print running_total(3)

def running_total(iterations):
    return sum(range(iterations,0,-1))


if __name__ == '__main__':
    main()
