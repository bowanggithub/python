def fact(n):
    '''
    Simple factorial function with doctest.

    >>> fact(4)
    24
    >>> fact(1)
    1
    >>> fact(0)
    Traceback (most recent call last):
        ...
            raise ValueError()
    ValueError
    '''
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)

if __name__=="__main__":
    import doctest
    doctest.testmod()
