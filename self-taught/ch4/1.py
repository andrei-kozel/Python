def f(x):
    """
    Takes an int and returnes it myltiplied by 2
    :param x: int,
    :return: x multiplied by 2 
    """
    return f"{x} x {x} = {x * x}"


x = input("Input a number: ")
x = int(x)
print(f(x))
