def calculate(op, x, y):
    if op == 'Addition':
        print(x+y)
        return x + y
    elif op == 'Subtract':
        print(x-y)
        return x - y
    elif op == 'Multiply':
        print(x*y)
        return x * y
    elif op == 'Divide':
        print(x/y)
        return x / y
    else:
        return 'Invalid Operation'
        