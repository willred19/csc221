def is_leap_year(year):
    if year %4 == 0 and year %100 != 0 or year % 400 == 0:
        return True
    else:
        return False
        '''
    >>> test_is_leap_year(2000)
    True
    >>> test_is_leap_year(1985)
    False
    >>> test_is_leap_year(2007)
    False
    >>> test_is_leap_year(2016)
    True
    >>> test_is_leap_year(2006)
    False
        '''