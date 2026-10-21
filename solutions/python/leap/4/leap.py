def leap_year(year):
    """ Caculate leap_year

    * In every year that is evenly divisible by 4.
    * Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
    """
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
