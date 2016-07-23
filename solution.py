import re

def answer(input):
    output = []
    operators = []
    
    multiply_operator = 10
    addition_operator = 5

    print "GIVEN: " + input

    for c in input:
        num_search = re.match('\d', c)

        if (re.match('\d', c)):
            print "Got number " + c + "; pushing to output";
            output.append(c)
        elif (re.match('[\*\+]', c)):
            print "Got operator..."
            current_operator = 0
            compare_operator = 0

            if (re.match('\*', c)):
                current_operator = multiply_operator
            elif (re.match('\+', c)):
                current_operator = addition_operator

            if ((len(operators) > 0) and (operators[0] == "*")):
                compare_operator = 10
            elif ((len(operators) > 0) and (operators[0] == "+")):
                compare_operator = 5
                

            if (current_operator <= compare_operator):
                print "  (" + current_operator + ") presendence is LESS THAN OR EQUAL TO operator at top of stack: " + str(compare_operator)
                print "    Pushing to output..."
                
                output.append(operators.pop(0))

            print "  Pushing (" + c + ") to OPERATOR stack..."
            operators.append(c)
    # END FOR LOOP

    output += operators
    print output


# MAIN

foo = "2+3*2"

#foo = "2*4*3+9*3+5"

answer(foo)
