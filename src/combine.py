import math
import itertools


def applyAll(fs, xs):
    '''
    calls the GenerateDataForOneFunction method for a list of functions and combines data
    '''
    ys = []
    for x in xs:
        ys.append(sum([f(x) for f in fs]))
    return ys


def add(xs1, xs2):
    return [x1 + x2 for (x1, x2) in zip(xs1, xs2)]