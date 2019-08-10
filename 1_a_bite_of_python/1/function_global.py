x = 50

def func():
    global x
    x=55
    print(f'Global X from function x = {x}')

print(f'X before calling func() with global X. x = {x}')
func()
print(f'X after func() x = {x}')