def square(number):
    if 64 >= number >= 1:
        return 2 ** (number - 1)
        
    raise ValueError("square must be between 1 and 64")


def total():
    return square(64) * 2 - 1
