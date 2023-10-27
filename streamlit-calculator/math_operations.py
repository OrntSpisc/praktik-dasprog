def add(x, y):
    """add
    Adds two numbers

    >>> add(3,5)
    8
    >>> add(4,6)
    10
    """

    return x + y


def subtract(x, y):
    """
    Subtracts y from x numbers

    >>> subtract(10,5)
    5
    >>> subtract(12,8)
    4
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers

    >>> multiply(4,6)
    24
    >>> multiply(5,4)
    20
    """

    return x * y


def divide(x, y):
    """
    Divides x by y

    >>> divide(8,4)
    2.0
    >>> divide(15,3)
    5.0
    """

    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

if __name__ == "__main__":
    import doctest
    doctest.testmod()