import operator

def basic_op(operat, value1, value2):
    op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }
    return op[operat](value1, value2)

print (basic_op('+', 4, 7))         # Output: 11
print (basic_op('-', 15, 18))       # Output: -3
print (basic_op('*', 5, 5))         # Output: 25
print (basic_op('/', 49, 7))        # Output: 7
