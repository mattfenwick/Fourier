from math import cos, sin, exp


def SineDecay(a, w, offset, t, tzero=0):
    '''
       -a - amplitude
       -w - frequency
       -offset - offset
       -t - time constant for exponential decay
    '''
    return lambda x: a * sin(((x + tzero) * w) + offset) * exp(-x * t)


def CosineDecay(a, w, offset, t, tzero=0):
    '''
       -a - amplitude
       -w - frequency
       -offset - offset
       -t - time constant for exponential decay
    '''
    return lambda x: a * cos(((x + tzero) * w) + offset) * exp (-x * t)


def complex(fr, fi):
    return lambda x: fr(x) + 1j * fi(x)


def csComplex(*args):
    return complex(CosineDecay(*args), SineDecay(*args))

