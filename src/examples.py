import math
import pylab
import random
import numpy
from . import dft
from . import combine
from . import ftime


_figure = 1
def newFigure():
    global _figure
    pylab.figure(_figure)
    _figure += 1

def plotC(cs):
    reals = map(lambda x: x.real, cs)
    imags = map(lambda x: x.imag, cs)
    pylab.plot(reals)
    pylab.plot(imags)


def eg6():
    '''
    complex time-domain data.  multiple frequencies
    '''
    f1 = ftime.sdComplex(5, 1.88, 0, 0.005)
    f2 = ftime.sdComplex(5, 5.37, 0, 0.005)
    f = lambda x: f1(x) + f2(x)
    
    ts = map(f, range(512))
    
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ft)

def eg7(pts=128):
    '''
    truncated complex time-domain data
    '''
    f = ftime.sdComplex(5, 1.88, 0, 0.005)
    
    ts = map(f, range(pts))
    
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ft)

def eg8(pts=256, zeroes=256):
    """
    complex zero fill
    """
    p1 = ftime.sdComplex(5, 1.88,  0, 0.005)
    
    xs = range(pts)
    
    t1 = map(p1, xs)
    t2 = t1 + [0 + 0j] * zeroes

    ft1 = dft.dft1d(t1)
    ft2 = dft.dft1d(t2)

    newFigure()
    plotC(t1)
    newFigure()
    plotC(t2)

    newFigure()
    plotC(ft1)
    newFigure()
    plotC(ft2)

def eg9(noise=1, pts=512):
    """
    complex gaussian noise
    """
    p1 = ftime.sdComplex(5, 1.88,  0, 0.005)
    
    xs = range(pts)
    
    t1 = map(p1, xs)
    t2 = numpy.random.normal(scale=noise, size=pts)
    ts = [o.real + nr + 1j * (o.imag + ni) for (o, nr, ni) in zip(t1, numpy.random.normal(scale=noise, size=pts), numpy.random.normal(scale=noise, size=pts))]

    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg10(pts=512):
    """
    complex out of phase (two sine waves -- no cosine)
    """
    p1 = ftime.sdComplex(5, 1.88,  0, 0.005)
    
    ts = [c.real + c.real * 1j for c in map(p1, range(pts))]
    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg11(decayRate=0.005, pts=512):
    """
    complex decay rate
    """
    p1 = ftime.sdComplex(5, 1.88,  0, decayRate)
    
    ts = map(p1, range(pts))
    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg12(maxGap=5, pts=512, decayRate=0.005):
    """
    complex: randomly set points to 0
    """
    p1 = ftime.sdComplex(5, 1.88,  0, decayRate)
    
    ts = map(p1, range(pts))
    
    ix = 0
    while True:
        ix += random.randint(1, maxGap)
        if ix >= len(ts):
            break
        ts[ix] = 0 + ts[ix].imag * 1j
    
    ix = 0
    while True:
        ix += random.randint(1, maxGap)
        if ix >= len(ts):
            break
        ts[ix] = ts[ix].real + 0j
    
    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg13(freqs=10, pts=512):
    """
    many complex frequencies
    """
    fs = []
    for i in range(freqs):
        amp = random.random() * 10
        omega = random.random() * 10
        dr = random.random() * 0.03
        fs.append(ftime.sdComplex(amp, omega, 0, dr))
    
    def f(x):
        return sum([f(x) for f in fs])
    
    ts = map(f, range(pts))
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ts)
    
    newFigure()
    pylab.plot([t.imag for t in ft])
#    plotC(ft)

def eg14(p1s=[], params=[(1, 2, .01)], pts=512):
    """
    many complex frequencies
    """
    fs = [ftime.sdComplex(float(amp), float(omega), 0, float(dr)) for (amp, omega, dr) in p1s + params]
    
    def f(x):
        return sum([f(x) for f in fs])
    
    ts = map(f, range(pts))
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ts)
    
    newFigure()
    pylab.plot([t.imag for t in ft])
#    plotC(ft)
