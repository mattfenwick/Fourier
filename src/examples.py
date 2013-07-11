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
    
plotFT = plotC


def eg1():
    """
    a non-decaying, real-only sine wave
    """
    newFigure()
    plotFT(combine.applyAll([math.sin], range(500)))

def eg2(a=1, w=0.5, offset=0, t=0.1):
    """
    a single real-only decaying sinusoid, plus its dft
    """
    p1 = ftime.SineDecay(a, w, offset, t)
    theData = combine.applyAll([p1], range(500))
    theFT = dft.dft1d(theData)

    newFigure()
    pylab.plot(theData)
    newFigure()
    plotFT(theFT)

def eg3():
    """
    combines a couple frequencies.  real-only data
    """
    p1 = ftime.SineDecay(5, 150,  0, 0.1)
    p2 = ftime.SineDecay(.3, 140, 0, 0.1)
    
    xs = range(500)
    
    t1 = map(p1, xs)
    t2 = map(p2, xs)
    tsum = combine.add(t1, t2)

    ft1 = dft.dft1d(t1)
    ft2 = dft.dft1d(t2)
    ftsum = dft.dft1d(tsum)

    newFigure()
    pylab.plot(t1)
    pylab.plot(t2)
    pylab.plot(tsum)

    newFigure()
    plotFT(ft1)
    newFigure()
    plotFT(ft2)
    newFigure()
    plotFT(ftsum)

def eg4():
    """
    shows effect of zero fill
    """
    p1 = ftime.SineDecay(5, .1,  0, 0.0025)
    
    xs = range(700)
    
    t1 = map(p1, xs)
    t2 = t1[:500] + [0] * 200
    tsum = combine.add(t1, t2)

    ft1 = dft.dft1d(t1)
    ft2 = dft.dft1d(t2)
    ftsum = dft.dft1d(tsum)

    newFigure()
    pylab.plot(t1)
    pylab.plot(t2)
    pylab.plot(tsum)

    newFigure()
    plotFT(ft1)
    newFigure()
    plotFT(ft2)
    newFigure()
    plotFT(ftsum)

def eg5():
    """
    shows effect of random noise.  poor noise function used
    """
    p1 = ftime.SineDecay(5, .1,  0, 0.005)
    
    t1 = map(p1, range(700))
    t2 = map(lambda x: x + random.random() * 2 - 1, t1)

    ft1 = dft.dft1d(t1)
    ft2 = dft.dft1d(t2)

    newFigure()
    pylab.plot(t1)
    pylab.plot(t2)

    newFigure()
    plotFT(ft1)
    newFigure()
    plotFT(ft2)

## END REAL-ONLY DATA

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
    # plotFT(ft)

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
