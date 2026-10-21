def steps(number):
    """ Collatz Conjecture

        Find how many steps to a number to converge to 1
    """
    
    if number > 0 and isinstance(number, int):

        if number == 1:
            return 0

        steps = 0
        while number > 1:
            print(number)
            if number % 2 == 0:
                number = number / 2
            else:
                number = (number * 3) + 1
            steps += 1
        return steps

    raise ValueError("Only positive integers are allowed")
