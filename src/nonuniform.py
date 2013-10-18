import numpy.random
import numpy.fft
from . import ftime
from . import wip


def fnoise(noise):
    return lambda _: numpy.random.normal(scale=noise) + 1j * numpy.random.normal(scale=noise)


def signal(amp, omega, t):
    offset = 0
    return ftime.csComplex(amp, omega, offset, t)


def full(amp, omega, t, noise):
    f1 = fnoise(noise)
    f2 = signal(amp, omega, t)
    return lambda x: f1(x) + f2(x)


def manySigs(params, noise):
    fs = [signal(amp, omega, t) for (amp, omega, t) in params]
    f1 = fnoise(noise)
    def g(x):
        sig = sum([f(x) for f in fs])
        return sig + f1(x)
    return g
    


def sample(f, dt, n):
    return [f(x * dt) for x in range(n)]


def sampleTr(tr, f, dt, n):
    series = [sample(f, dt, n) for _ in range(tr)]
    print 'tr: ', sum(map(len, series))
    return map(sum, zip(*series))


def sampleWeighted(f, dt, n):
    xs = []
    total = 0
    for x in range(n):
        pts = n - x
        total += pts
        xs.append(sum([f(x * dt) for _ in range(pts)]))
    print 'weighted: ', total
    return xs


def plot(ts):
    ft = numpy.fft.fft(ts)
    wip.newFigure()
    wip.plotC(ts)
    wip.newFigure()
    wip.plotC(ft)
    return ft
    

def example(noise=3, pts=512):
    params = [(1, 2, 0.1), (1, 14, 0.5), (1, 32, 0.5), (1, 33, 0.5)]
    dt = 0.1
#    sig = full(1, 2, .1, noise)
    sig = manySigs(params, noise)
    ts = sample(sig, dt, pts)
    ft = plot(ts)
    
    ts8 = sampleTr(257, sig, dt, pts)
    ft8 = plot(ts8)
    
    tsW = sampleWeighted(sig, dt, pts)
    ftW = plot(tsW)
    
    tsClean = sample(manySigs(params, 0.0001), dt, pts)
    ftClean = plot(tsClean)
