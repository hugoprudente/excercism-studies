def triagle_inequality(a, b, c):
    return a <= b + c and b <= c + a and c <= a + b

def equilateral(sides):
    a, b, c = sides
    if triagle_inequality(a, b, c):
        if a == 0 and b == 0 and c == 0:
            return False 
            
        if a == b and b == c and c == a:
            return True
    return False


def isosceles(sides):
    a, b, c = sides
    if triagle_inequality(a, b, c):
        if a == b or a == c or b == c:
            return True
    return False


def scalene(sides):
    a,b,c = sides
    if triagle_inequality(a, b, c):
        if b == c or a == c or a == b:
            return False
        return not equilateral(sides)            
    return False