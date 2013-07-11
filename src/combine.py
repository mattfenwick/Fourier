import math
import itertools


def applyAll(fs, xs):
    '''
    apply a list of functions to a list of x-values
    '''
    ys = []
    for x in xs:
        ys.append(sum([f(x) for f in fs]))
    return ys


def add(xs1, xs2):
    return [x1 + x2 for (x1, x2) in zip(xs1, xs2)]