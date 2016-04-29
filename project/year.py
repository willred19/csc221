def is_leap_year(year):
    '''
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1985)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2007)
    False
    >>> is_leap_year(2016)
    True
    >>> is_leap_year(2006)
    False
    '''
    if year %4 == 0 and year %100 != 0 or year % 400 == 0:
        return True
    else:
        return False
