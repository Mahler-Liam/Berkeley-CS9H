import argparse

def decimal_to_binary(x):
    """
    This function converts a decimal number N into a binary number with 8 bits.
    :param x: The decimal number

    >>> decimal_to_binary(30)
    '00011110'
    >>> decimal_to_binary(139)
    '10001011'
    """
    assert 0 <= x <= 255
    # START OF YOUR CODE
    binary_rule = ''
    for i in range(8):
        binary_rule = str(x%2) + binary_rule
        x = (int)(x/2)

    return binary_rule
         
    # END OF YOUR CODE


def generate(rule, steps):
    """
    Generate the image from given rule number and steps
    and print it to the console.
    The output image should have width of 2 * STEPS + 1 and height of STEPS + 1.

    :param rule: The rule number
    :param steps: Number of lines

    >>> generate(30, 5)
    P1 11 6
    0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0 0
    0 0 0 1 1 0 0 1 0 0 0
    0 0 1 1 0 1 1 1 1 0 0
    0 1 1 0 0 1 0 0 0 1 0
    1 1 0 1 1 1 1 0 1 1 1
    """
    # START OF YOUR CODE
    width = 2*steps + 1
    height = steps + 1
    
    print("P1 %d %d" % (width, height))
    zeroline = generate_zeroline(steps)
    line = [0] * (steps+1)
    line[0] = zeroline
    for i in range(steps):
        line[i+1] = generate_line(rule, steps, line[i])

    for i in range(steps+1):
        print(line[i])


    # END OF YOUR CODE


# TODO: You may add any additional functions here

def generate_zeroline(steps):
    #zerolist = [0] * (2*steps+1)
    zerolist = list()
    for i in range(2*steps+1):
        if i == (steps) :
            #zerolist[i] = 1
            zerolist.append(1)
        else :
            #zerolist[i] = 0
            zerolist.append(0)
    zeroline = ' '.join(str(num) for num in zerolist)
    return zeroline


def generate_line(rule, steps, inputline):
    def generate_cell(number):
        binary_rule_string = decimal_to_binary(rule)
        according_string = [0] * 8
        for i in range(8):
            according_string[i] = binary_rule_string[7-i]
        return according_string[number]
     
    new_inputline = '0' + inputline.replace(' ','') + '0'
    outputline = [0] * (2*steps+1)

    for i in range(2*steps+1):
        outputline[i] = generate_cell(int(new_inputline[i:i+3],2))

    outputstring = " ".join(str(num) for num in outputline)
    return outputstring


if __name__ == '__main__':
    # START OF YOUR CODE
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Project 1: Cellular Automaton')
    parser.add_argument('rule', help='The Rule', type=int)
    parser.add_argument('steps', help='Number of Steps', type=int)
    args = parser.parse_args()
    rule, steps = args.rule, args.steps

    # END OF YOUR CODE

    assert 0 <= rule <= 255 and steps >= 0
    generate(rule, steps)
