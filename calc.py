#Step_1
def calc(op, A, B) :
    if op == '+' :
        return A+B
    elif op == '-' :
        return A-B
    elif op == '/' :
        return A/B
    elif op == 'x' :
        return A*B


#Step_2
with open('step_2.txt', 'r') as f:
    result = 0
    calc_input = f.read().splitlines()
    for line in calc_input:
        call, op, input1, input2 = line.split(' ')
        result = result + calc(op, int(input1), int(input2))
        
    print(result)

