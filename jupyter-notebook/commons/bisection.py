# Python implementation of Sauer's Bisection 

def bisect(func, a, b, tol):
    fa = func(a)
    fb = func(b)
    if fa*fb >= 0:
        quit()
        
    while (b-a)/2 > tol:
        c = (a+b)/2
        fc = func(c)
        if fc == 0:
            return c
        elif fc*fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a+b)/2