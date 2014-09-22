import math
import pylab
import random
import numpy
from . import ftime
from . import examples as e
from . import sampler


_figure = 1
def newFigure():
    global _figure
    pylab.figure(_figure)
    val = _figure
    _figure += 1
    return val

def plotC(cs):
    reals = map(lambda x: x.real, cs)
    imags = map(lambda x: x.imag, cs)
    y = pylab.plot(reals)
    z = pylab.plot(imags)
    print y, z
    return y


def split(cs):
    real, imag = [], []
    for c in cs:
        real.append(round(c.real, 3))
        imag.append(round(c.imag, 3))
    return real, imag


def dump(ts, ft):
    tr, ti = split(ts)
    fr, fi = split(ft)
    print '\n        '.join(['      {', 
                             '"time": [', str(tr) + ',', str(ti), '], ', 
                             '"freq": [', str(fr) + ',', str(fi), ']',
                             '}'])


def splitAdd(f, *fs):
    def g(*args, **kwargs):
        return sum([h(*args, **kwargs) for h in (f,) + fs])


def sampleFtAndDisplay(ts):
    newFigure()
    plotC(ts)

    ft = numpy.fft.fft(ts) # scale 1st point?
    newFigure()
    plotC(ft)
    
    dump(ts, ft)
    return ft


def vanilla(amp=1, w=1, offset=0, dr=0.005, pts=512):
    '''
    complex time-domain.  single frequency
    '''
    f = ftime.csComplex(amp, w, offset, dr)
    
    return map(f, range(pts))


FREQ = 0.3


standard = vanilla(w=FREQ)


def basics():
    sampleFtAndDisplay(vanilla(w=FREQ, dr=0))
    sampleFtAndDisplay(vanilla(w=0))
    sampleFtAndDisplay(standard)


def linearity():
    f1 = ftime.csComplex(1, 0.1, 0, 0.005)
    f2 = ftime.csComplex(1, FREQ, 0, 0.005)
    f = lambda x: f1(x) + f2(x)
    
    sampleFtAndDisplay(map(f1, range(512)))
    sampleFtAndDisplay(map(f2, range(512)))
    sampleFtAndDisplay(map(f, range(512)))


def decay_rate():
    sampleFtAndDisplay(standard)
    sampleFtAndDisplay(vanilla(w=FREQ, dr=0.03))


def acquisition_time():
    sampleFtAndDisplay(standard)
    sampleFtAndDisplay(vanilla(w=FREQ, pts=128))


def amplitude():
    sampleFtAndDisplay(standard)
    sampleFtAndDisplay(vanilla(w=FREQ))
