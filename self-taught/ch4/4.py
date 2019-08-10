def devide(x):
    """
    Takes int and devide it by 2. And pass result to multiply function


    :param x: int,
    :result: x devided by 2
    """
    result = x / 2
    multiply(result)


def multiply(x):
    """
    Takes int and myltiply it by 4. 

    :param x: int,
    :result: x myltiplied by 4
    """
    result = x * 4
    print(f"result: {result}")


devide(2)
devide(20)
devide(12)
