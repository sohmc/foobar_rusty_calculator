import re
import subprocess

def answer(str):
#    DEBUG = 0  # Uncomment when submitting
    output = []
    operators = []
    
    multiply_operator = 10
    addition_operator = 5

    if DEBUG > 5: print "GIVEN: " + str

    # Using the Shunting-yard method
    for c in str:
        # Step 1: evaluate the token
        num_search = re.match('\d', c)

        # Step 1.a: If it's a number, push to output
        if (re.match('\d', c)):
            if DEBUG > 0: print "Got number " + c + "; pushing to output"
            output.append(c)
            if DEBUG > 5: print output

        # Step 1.b: if it's an operator..
        elif (re.match('[\*\+]', c)):
            if DEBUG > 0: print "Got operator (" + c + ")"
            current_operator = 0
            compare_operator = 0

            if (re.match('\*', c)):
                current_operator = multiply_operator
            elif (re.match('\+', c)):
                current_operator = addition_operator
            
            # Steb 1.b.a: While there is an operator on the operator
            #             stack...
            while (len(operators) > 0):
                top_operator = len(operators) - 1
                if (operators[top_operator] == "*"):
                    compare_operator = 10
                elif (operators[top_operator] == "+"):
                    compare_operator = 5

                # Step 1.b.a.a: if the incoming operator is less than or
                #               equal to the top operator...
                # MODIFICATION FOR GOOGLE: In order to get the largest
                # lexigraphical value, check if it's only LESS THAN
                if (current_operator < compare_operator):
                    if DEBUG > 5: 
                        print "  (" + c + ") presendence is LESS THAN the operator at top of stack: " + operators[top_operator]
                        print "    Pushing (" + operators[top_operator] + ") to output..."

                    # Step 1.b.a.b: Push the top operator to output
                    output.append(operators.pop())
                else:
                    break
            # END WHILE LOOP

            # Step 1.b.b: Push the current operator on top of the stack
            if DEBUG > 0: print "  Pushing (" + c + ") to OPERATOR stack..."
            operators.append(c)
            if DEBUG > 5: print operators
    # END FOR LOOP

    # Step 2: If there are no more tokens to read but there are
    #         operators in the stack:
    if (len(operators) > 0):
        operators.reverse()
        output += operators

    if DEBUG > 0: 
        print output
        print " ".join(output)
        return output
    else: 
        return "".join(output)

    


# MAIN
DEBUG = 10

problems = {"2+3*2": "232*+", 
            "2*4*3+9*3+5": "243**93*5++",
            "7*8+4+1*5*9+4*2+1": "78"
            }


i = 0
for foo, ans in problems.items():
    print " -------- BEGIN " + str(i) + " --------"
    rpn = answer(foo)
    if DEBUG > 0: 
        print "INPUT:      " + foo
        print "Response:   " + "".join(rpn)
        print "Should be:  " + ans

        rpn.append("p");
        dc_input = " ".join(rpn)
        print " -- "
        dc_output = subprocess.check_output('dc -e "' + dc_input + '"', shell=True)
        bc_output = eval(foo)
        print "dc output:     " + dc_output.rstrip('\n')
        print "python output: " + str(bc_output)

    i += 1;

