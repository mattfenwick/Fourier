from math import cos, sin, exp


class SineDecay(object):

    def __init__(self, a, w, offset, t, tzero=0):
       '''
       -a - amplitude
       -w - frequency
       -offset - offset
       -t - time constant for exponential decay
       '''
       self.a = a
       self.w = w
       self.offset = offset
       self.t = t
       self.tzero = tzero
       
    def __call__(s, x):
        return s.a * sin(((x + s.tzero) * s.w) + s.offset) * exp (-x * s.t)


class CosineDecay(object):

    def __init__(self, a, w, offset, t, tzero=0):
       '''
       -a - amplitude
       -w - frequency
       -offset - offset
       -t - time constant for exponential decay
       '''
       self.a = a
       self.w = w
       self.offset = offset
       self.t = t
       self.tzero = tzero
       
    def __call__(s, x):
        return s.a * cos(((x + s.tzero) * s.w) + s.offset) * exp (-x * s.t)


class ComplexDecay(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self, t):
        return self.x(t) + (1j * self.y(t))


def sdComplex(a, w, o, t, tzero=0):
#    s = SineDecay(a, w, o, t, tzero)
#    c = CosineDecay(a, w, o, t, tzero)
#    def f(x):
#        return s(x) + (1j * c(x))
#    return f
    return ComplexDecay(SineDecay(a, w, o, t, tzero), CosineDecay(a, w, o, t, tzero))


def csComplex(*args):
    return ComplexDecay(CosineDecay(*args), SineDecay(*args))

