def calculator(operator:str, *args):

    """calculator

    ## Parameters
    operator (string): Operator
    *args (tuple(int, float)): Numbers to operate

    ## Returns
    accumulator (int, float): Result of the operation

    ## Raises
    ValueError

    ## Example
    print(calculator('*', 1.9,2.3,3,4,5)) # Output 262.19999999999993

    """
    if len(args) == 0:
        raise ValueError("No number entered")
    if len(args) == 1:
        return args[0]
    if not all((type(i) == int or type(i) == float) for i in args):
        raise ValueError("One or more input invalid")

    accumulator = args[0]
    
    if operator == '+':
        for num in args[1:]:
            accumulator += num
    elif operator == '-':
        for num in args[1:]:
            accumulator -= num
    elif operator == '*':
        for num in args[1:]:
            accumulator *= num
    elif operator == '/':
        for num in args[1:]:
            accumulator /= num
    else:
        raise ValueError("Invalid operator")
    return accumulator


print(calculator('+', 1,2,3,4,5)) # Output 15.9
print(calculator('-', 10.2,9.5,8,7,6)) # Output -20.3
print(calculator('*', 1.9,2.3,3,4,5)) # Output 262.19999999999993
print(calculator('/', 100,10,2.5)) # Output 4.0
