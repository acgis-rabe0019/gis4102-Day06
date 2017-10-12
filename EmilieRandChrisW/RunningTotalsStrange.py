#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     10-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    print strange_sum(3)
    print strange_sum(154)
    print strange_sum(4)

def strange_sum(number):
    denominator = number
    sum = 0
    for numerator in range(1, number + 1):
        sum += float(numerator) / denominator
        denominator -= 1
    return sum



if __name__ == '__main__':
    main()