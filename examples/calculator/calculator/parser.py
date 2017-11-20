import re

def parser_mult(input_str):
    pattern = r"[\d.]+|[\*\/]"
    match = re.findall(pattern, input_str)

    if not len(match)&1:
        raise Exception("Error")

    result = float(match[0])

    for i in range(1, len(match), 2):
        if match[i] == '*':
            result *= float(match[i+1])
        if match[i] == '/':
            result /= float(match[i+1])

    return result

def parser(input_str):
    pattern = r"[\w.\*\/]+|[\+\-]"
    match = re.findall(pattern, input_str)

    if not len(match)&1:
        raise Exception("Error")

    result = parser_mult(match[0])

    for i in range(1, len(match), 2):
        if match[i] == '+':
            result += parser_mult(match[i+1])
        if match[i] == '-':
            result -= parser_mult(match[i+1])

    return result

if __name__ == "__main__":
    try:
        print(parser("2.56+5*9/1+9*7"))
    except:
        print("Error")
    #m = parser("2.56+5+9.7")
    print(2.56+5*9/1+9*7)
