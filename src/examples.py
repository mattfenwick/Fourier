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

def addFs(fs):
    """
    [a -> b] -> a -> b
    """
    return lambda x: sum([f(x) for f in fs])

def eg5(w=0.1):
    '''
    complex time-domain.  single frequency
    '''
    f = ftime.sdComplex(5, w, 0, 0.005)
    
    ts = map(f, range(512))
    
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ft)
    
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

def eg7(w=1.88, dr=0.0005, pts=2048):
    '''
    truncated complex time-domain data
    '''
    f = ftime.sdComplex(5, w, 0, dr)
    
    ts = map(f, range(pts))
    
    newFigure()
    plotC(ts)
    
    ft = numpy.fft.fft(ts)
    
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

def eg9(noise=1, dr=0.005, pts=512):
    """
    complex gaussian noise
    """
    p1 = ftime.sdComplex(5, 1.88,  0, dr)
    
    xs = range(pts)
    
    t1 = map(p1, xs)
    t2 = numpy.random.normal(scale=noise, size=pts)
    ts = [o.real + nr + 1j * (o.imag + ni) for (o, nr, ni) in zip(t1, numpy.random.normal(scale=noise, size=pts), numpy.random.normal(scale=noise, size=pts))]

    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)

def eg10(offset=0, omega=0.0839, dr=0.005, pts=512):
    """
    complex out of phase (two sine waves -- no cosine)
    offset:  number of periods out of phase.  nmr data is normally 1/4 period out of phase, I think
    """
    amp = 5
    r = ftime.SineDecay(amp, omega, offset * 2 * math.pi, dr)
    i = ftime.CosineDecay(amp, omega, 0, dr)
    def f(x):
        return r(x) + 1j * i(x)
    
    ts = map(f, range(pts))
    
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

def eg18(g1=1.0, g2=5.0, g3=-1.0, sw=6000.0, dr=0.005, pts=512):
    """
    lorentz-to-gauss windowing function, based on nmrpipe's gm function
    """
    p1 = ftime.sdComplex(5, 1.88,  0, dr)
    
    ts = map(p1, range(pts))
    
    def f(i):
        something = math.pi * i * g1 / sw
        g = 0.6 * math.pi * g2 * (g3 * (pts - 1) - i) / sw
        return math.e ** (something - g * g)
    
    xs = [t * f(i) for (i, t) in enumerate(ts)]
    newFigure()
    plotC(xs)
    
    ft = dft.dft1d(xs)
    newFigure()
    plotC(ft)

def eg19(o=math.pi/4., omega=1, omega2=5.14, dr=0.01, pts=2048):
    """
    zero-order phase correction
    the default offset splits the "good" part of the signal evenly between the two channels.
      `0` would put it all in one channel, and `pi / 2` would put it all in the other
    """
    p1 = ftime.sdComplex(5, omega, o, dr)
    p2 = ftime.sdComplex(3, omega2, o, dr)
    
    ts = map(lambda x: p1(x) + p2(x), range(pts))
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    newFigure()
    plotC(ft)

def eg20(tzero=1, w1=1, w2=5.14, pts=512):
    """
    1st-order phase correction
    """
    p1 = ftime.sdComplex(5, w1, 0, 0.01, tzero)
    p2 = ftime.sdComplex(4, w2, 0, 0.01, tzero)
    
    ts = map(lambda x: p1(x) + p2(x), range(pts))
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    newFigure()
    plotC(ft)

def eg21(transients=5, noise=1, dr=0.02, pts=512):
    """
    Three peaks:  
      1) fast decay, high amplitude
      2) slow decay + high amplitude
      3) slow decay + low amplitude
    then add in noise, see which peaks are hard to distinguish
    then do multiple transients, see how the peaks reappear
    """
    p1 = ftime.sdComplex(50, 5.32, 0, dr * 10)
    p2 = ftime.sdComplex(50, 1.88, 0, dr)
    p3 = ftime.sdComplex(2, 3.89, 0, dr)
    f = addFs([p1, p2, p3])
    
    xs = range(pts)
    
    yseries = []
    for _ in range(transients):
        t1 = map(f, xs)
        t2 = numpy.random.normal(scale=noise, size=pts)
        ts = [o.real + nr + 1j * (o.imag + ni) for (o, nr, ni) in zip(t1, numpy.random.normal(scale=noise, size=pts), numpy.random.normal(scale=noise, size=pts))]
        yseries.append(ts)
    
    ts = map(sum, zip(*yseries))

    ft = dft.dft1d(ts)
    
    sums, tot, smallest = [], 0, min([y.imag for y in ft])
    for x in ft:
        tot += x.imag - smallest # substract the 'baseline'
        sums.append(tot)
    
    newFigure()
    pylab.plot(sums)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)
