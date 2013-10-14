import pylab
import numpy
from . import ftime
from . import wip


_figure = 1
def newFigure():
    global _figure
    pylab.figure(_figure)
    val = _figure
    _figure += 1
    return val

def plotC(xs, cs):
    reals = map(lambda x: x.real, cs)
    imags = map(lambda x: x.imag, cs)
    y = pylab.plot(xs, reals)
    z = pylab.plot(xs, imags)
    rs  = str(map(list, zip(xs, map(lambda x: round(x, 3), reals))))
    ims = str(map(list, zip(xs, map(lambda y: round(y, 3), imags))))
    print '[', rs, ', \n      ', ims, ']\n'


def sample(f, width, start, pts):
    """
    from `start` to `start + width` in `pts` increments
    start + i * width / n
    """
    def g(i):
        return start + float(i) * float(width) / float(pts)
    return [f(g(t)) for t in range(pts)]


def eg1():
    f1 = ftime.csComplex(1, 10, 0, .05)
    f2 = ftime.csComplex(1, 2, 0, .05)
#    f = lambda x: f1(x) + f2(x)
    f = f1
    
    ts1 = sample(f, 128, 0, 128)
    ts2 = sample(f, 128, 0, 256)
    ts3 = sample(f, 128, 0, 512)
    ts4 = sample(f, 128, 0, 16384)
    ts5 = sample(f, 128, 0, 2048)
    
    ft1 = numpy.fft.fft(ts1)
    ft2 = numpy.fft.fft(ts2)
    ft3 = numpy.fft.fft(ts3)
    ft4 = numpy.fft.fft(ts4)
    ft5 = numpy.fft.fft(ts5)
    
    newFigure()
    plotC(range(0, 128, 1), ts1)
    plotC([float(x) / 2.0 for x in range(0, 256)], ts2)
    plotC([float(x) / 4.0 for x in range(0, 512)], ts3)
#    plotC([float(x) / 128.0 for x in range(0, 16384)], ts4)
#    plotC([float(x) / 16.0 for x in range(0, 2048)], ts5)
    
    newFigure()
    plotC(range(128), ft1)
    plotC(range(256), ft2)
    plotC(range(512), ft3)
#    plotC(range(16384), ft4)
#    plotC(range(2048), ft5)


def resolution():
    f1 = ftime.csComplex(1, 1, 0, 0.05)
    f2 = ftime.csComplex(1, 1.1, 0, 0.05)
    f3 = lambda x: f1(x) + f2(x)
    
    ts1 = sample(f3, 128, 0, 128)
    ts2 = sample(f3, 128, 0, 512)
