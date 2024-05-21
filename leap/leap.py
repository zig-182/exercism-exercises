def leap_year(year):
    """
    A leap year is a year that is evenly divided by 4,
    unless the year is evenly divisible by 100, 
    in which case it's only a leap year if the year is also evenly divisible by 400.
    """

    #split it into three statements
       
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False