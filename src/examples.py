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
    val = _figure
    _figure += 1
    return val

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
    many complex frequencies, randomly generated
    """
    def pos(frequency):
        return (pts - frequency * pts / (2 * math.pi)) % pts
    
    fs = []
    params = []
    for i in range(freqs):
        amp = random.random() * 6.2 # let's keep it less than 2 * pi so there's no folding
        omega = random.random() * 10
        dr = random.random() * 0.03
        fs.append(ftime.sdComplex(amp, omega, 0, dr))
        params.append((pos(omega), omega, amp, dr))
    
    def f(x):
        return sum([f(x) for f in fs])
    
    ts = map(f, range(pts))
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ts)
    
    newFigure()
    pylab.plot([t.imag for t in ft])
#    plotC(ft)
    sortedParams = sorted(params, key=lambda x: x[0])
    print 'position, frequency, amplitude, decay rate:'
    for ps in sortedParams:
        print '    '.join(map(str, ps))

def eg14(p1s=[], params=[(1, 2, .01)], pts=512):
    """
    many complex frequencies, user supplied
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

def eg15(pts=512):
    """
    forward ft, then ft on results
    """
    f = ftime.sdComplex(1.1, 2.3, 0, .005)
    
    ts = map(f, range(pts))
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    newFigure()
    plotC(ft)
    
    ts2 = dft.dft1d(ft)
    newFigure()
    plotC(ts2)
    
    ft2 = dft.dft1d(ts2)
    newFigure()
    plotC(ft2)
    
    ts3 = dft.dft1d(ft2)
    newFigure()
    plotC(ts3)

def eg16(transients=5, noise=1, pts=512):
    """
    complex gaussian noise with multiple transients
    """
    p1 = ftime.sdComplex(5, 1.88,  0, 0.005)
    
    xs = range(pts)
    
    yseries = []
    for _ in range(transients):
        t1 = map(p1, xs)
        t2 = numpy.random.normal(scale=noise, size=pts)
        ts = [o.real + nr + 1j * (o.imag + ni) for (o, nr, ni) in zip(t1, numpy.random.normal(scale=noise, size=pts), numpy.random.normal(scale=noise, size=pts))]
        yseries.append(ts)
    
    ts = map(sum, zip(*yseries))

    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg17(params, extra=[(4, 2.5, .001), (4, 2.5, .003), (4, 2.5, .01), (4, 2.5, .03), (4, 2.5, .1)], pts=512):
    """
    more user-defined parameterization.
    plus default values showing that decay rate has no effect on peak position
    plots all time-domain data in one chart, and all ft data in a second chart (ignores reals)
    """
    xs = range(pts)
    
    yseries = []
    for (amp, omega, dr) in params + extra:
        f = ftime.sdComplex(amp, omega, 0, dr)
        yseries.append(map(f, xs))
    
    m, n = newFigure(), newFigure()
    for ys in yseries:
        pylab.figure(m)
        plotC(ys)
        pylab.figure(n)
        # plotC(dft.dft1d(ys))
        pylab.plot([pt.imag for pt in dft.dft1d(ys)])
