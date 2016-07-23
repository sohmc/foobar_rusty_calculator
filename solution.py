import re

def answer(str):
#    DEBUG = 0  # For Submission
    output = []
    operators = []
    
    multiply_operator = 10
    addition_operator = 5

    if DEBUG > 5: print "GIVEN: " + str

    for c in str:
        num_search = re.match('\d', c)

        if (re.match('\d', c)):
            if DEBUG > 0: print "Got number " + c + "; pushing to output"
            output.append(c)
            if DEBUG > 5: print output
        elif (re.match('[\*\+]', c)):
            if DEBUG > 0: print "Got operator (" + c + ")"
            current_operator = 0
            compare_operator = 0

            if (re.match('\*', c)):
                current_operator = multiply_operator
            elif (re.match('\+', c)):
                current_operator = addition_operator

            while (len(operators) > 0):
                if (operators[len(operators) - 1] == "*"):
                    compare_operator = 10
                elif (operators[len(operators) - 1] == "+"):
                    compare_operator = 5

                if (current_operator <= compare_operator):
                    if DEBUG > 5: print "  (" + c + ") presendence is LESS THAN OR EQUAL TO operator at top of stack: " + operators[0]
                    if DEBUG > 5: print "    Pushing (" + operators[0] + ") to output..."
                    output.append(operators.pop())
                else:
                    break
            # END WHILE LOOP

            if DEBUG > 0: print "  Pushing (" + c + ") to OPERATOR stack..."
            operators.append(c)
            if DEBUG > 5: print operators
    # END FOR LOOP

    output += operators
    if DEBUG > 0: print output
    print "".join(output)

    


# MAIN
DEBUG = 10

foo = "2*4*3+9*3+5"
foo = "2+3*5+1+2+7*4"
foo = "3+4*2*1+5"

answer(foo)
if DEBUG > 0: print foo
