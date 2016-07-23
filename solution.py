import re

def answer(str):
    print "GIVEN: " + str

    for c in str:
        num_search = re.match('\d', c)

        if (re.match('\d', c)):
            print "Got number: " + c
        elif (re.match('\*', c)):
            print "Got muliply"
        elif (re.match('\+', c)):
            print "Got plus"


# MAIN

foo = "2+3*2"

#foo = "2*4*3+9*3+5"

answer(foo)
