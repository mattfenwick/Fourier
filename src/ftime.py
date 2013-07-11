from math import cos, sin, exp


class SineDecay(object):

    def __init__(self, a, w, offset, t):
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
       
    def __call__(s, x):
        return s.a * sin((x * s.w) + s.offset) * exp (-x * s.t)


class CosineDecay(object):

    def __init__(self, a, w, offset, t):
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
       
    def __call__(s, x):
        return s.a * cos((x * s.w) + s.offset) * exp (-x * s.t)


def sdComplex(a, w, o, t):
    s = SineDecay(a, w, o, t)
    c = CosineDecay(a, w, o, t)
    def f(x):
        return s(x) + (1j * c(x))
    return f
