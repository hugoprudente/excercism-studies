def square(number):
    if 64 >= number >= 1:
        if number == 1:
            return 1
        if number == 2:
            return 2

        grain = 2
        for x in range(number - 2):  
            grain = grain * 2
            
        return grain
        
    raise ValueError("square must be between 1 and 64")


def total():
    return square(64) * 2 - 1
