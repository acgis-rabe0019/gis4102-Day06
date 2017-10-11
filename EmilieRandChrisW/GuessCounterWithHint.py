#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     11-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint
def main():
    print get_guess_count(11,1,20)
    print get_guess_count(11,1,20)
    print get_guess_count(11,1,20)
    print get_guess_count(11,1,20)

def get_guess_count(number_to_guess, min_bound, max_bound):
    number=randint(min_bound,max_bound)
    guesses=1
    if number >= min_bound and number<= max_bound:
        while number!=number_to_guess:
            number= randint(min_bound,max_bound)
            if number==number_to_guess:
                return "Your number is "+ str(number) + ". It took "+str(guesses)+" guesses to get this number."
            elif number != number_to_guess:
                guesses +=1
                if number<number_to_guess:
                    min_bound==number+1
                if number>number_to_guess:
                    max_bound==number-1
                if guesses>=100000:
                    return 'Guesses greater than 100000'
                if guesses>=100000:break
                else: continue

    else:
        return 0
if __name__ == '__main__':
    main()
