def f(a, b, c, d=4, e=5):
    """
    Prints paramters passed in. a,b,c are required parameters and d,e are optional. 
    Returnes string with passed parameters

    :param a: int,
    :param b: int,
    :param c: int,
    :param d: int,
    :param e: int
    """
    return f"a={a}, b={b}, c={c}, d={d}, e={e}"


print(f(1, 3, 4))
print(f(1, 3, 4, 12, 23))
