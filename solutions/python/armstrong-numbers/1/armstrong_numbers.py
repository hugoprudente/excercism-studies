def is_armstrong_number(number):
    """ Armstrong Number"""

    if number == 0:
        return True
        
    digest = len(str(number))
    armstrong_number = 0
    for num in str(number):
        armstrong_number += pow(int(num), digest)
    
    if number == armstrong_number:
        return True

    return False
