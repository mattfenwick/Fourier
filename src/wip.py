import math
import pylab
import random
import numpy
from . import dft
from . import combine
from . import ftime
from . import examples as e


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


def vanilla(amp=5, w=1, offset=0, dr=0.005, pts=512):
    '''
    complex time-domain.  single frequency
    '''
    f = ftime.sdComplex(amp, w, offset, dr)
    
    ts = map(f, range(pts))
    
    newFigure()
    plotC(ts)
    
    ft = dft.dft1d(ts)
    
    newFigure()
    plotC(ft)


def zeroes(pts=256, zs=256):
    """
    complex zero fill
    """
    p1 = ftime.sdComplex(5, 1.88,  0, 0.005)
    
    xs = range(pts)
    
    t1 = map(p1, xs)
    ts = t1 + [0 + 0j] * zs

    ft = dft.dft1d(ts)

    newFigure()
    plotC(ts)

    newFigure()
    plotC(ft)


def real_only():
    f = ftime.SineDecay(5, 0.1, 0, 0.005)
    ts = map(f, range(512))
    
    newFigure()
    pylab.plot(ts)
    
    ft = numpy.fft.rfft(ts)
    
    newFigure()
    plotC(ft)


def simple():
    vanilla(w=0.1)


def width():
    vanilla(dr=0.005)
    vanilla(dr=0.015)
    vanilla(dr=0.045)


def truncation():
    vanilla(pts=128)
    vanilla(pts=256)
    vanilla(pts=512)
    vanilla(pts=1024)


def amplitude():
    vanilla(amp=1)
    vanilla(amp=5)


def shift():
    vanilla(w=0.1)
    vanilla(w=2)
    vanilla(w=4)
    vanilla(w=6)
    vanilla(w=8)


def noise():
    e.eg9(100)
    e.eg9(10)
    e.eg9(1)
    e.eg9(.1)


def transients():
    e.eg21(1, 50)
    e.eg21(10, 50)
    e.eg21(100, 50)
    e.eg21(1000, 50)
    e.eg21(10000, 50)


def multiple_frequencies():
    e.eg13(1)
    e.eg13(4)
    e.eg13(16)
    e.eg13(64)


def zero_fill():
    zeroes(zs=0)
    zeroes(zs=256)
    zeroes(zs=768)


points = [[28401.0, -30544.0], [35571.0, 20461.0], [-15908.0, 36725.0], [-27780.0, -8137.0], [3278.0, -18585.0], [10661.0, 3102.0], [-2001.0, 8549.0], [-5011.0, 292.0], [-771.0, 98.0], [872.0, 1863.0], [-1411.0, 4157.0], [-3835.0, 393.0], [-711.0, -535.0], [415.0, 3944.0], [-3511.0, 3308.0], [-4175.0, -292.0], [404.0, -1377.0], [226.0, 4154.0], [-4247.0, 3328.0], [-4301.0, -709.0], [-1366.0, -1326.0], [-582.0, 1254.0], [-2161.0, 2974.0], [-2616.0, -381.0], [-1002.0, -117.0], [-1639.0, 2246.0], [-4454.0, -263.0], [-1148.0, -2759.0], [1002.0, 2098.0], [-3764.0, 3578.0], [-5494.0, -1741.0], [-2641.0, -3126.0], [830.0, -617.0], [-2149.0, 2179.0], [-4831.0, -1006.0], [-3144.0, -1365.0], [-2112.0, 422.0], [-3418.0, -723.0], [-2872.0, -2355.0], [-797.0, -2139.0], [-1860.0, -618.0], [-3287.0, 432.0], [-5452.0, -1888.0], [-1202.0, -2510.0], [770.0, -263.0], [-2099.0, 1994.0], [-5574.0, -1995.0], [-1612.0, -3916.0], [706.0, 652.0], [-2552.0, 3246.0], [-6475.0, -805.0], [-1976.0, -3692.0], [794.0, -1784.0], [-1977.0, 2046.0], [-4817.0, -1579.0], [-1085.0, -3394.0], [317.0, 1625.0], [-3969.0, 944.0], [-4491.0, -2236.0], [-1277.0, -3011.0], [769.0, -967.0], [-1767.0, 1152.0], [-4081.0, -1102.0], [-3393.0, -2098.0], [-737.0, -3228.0], [20.0, 705.0], [-2887.0, -145.0], [-1776.0, -2325.0], [244.0, -1734.0], [-1686.0, 44.0], [-2977.0, -2394.0], [-29.0, -3045.0], [-453.0, 1107.0], [-2699.0, 466.0], [-2052.0, -1275.0], [-1255.0, -847.0], [-1047.0, 27.0], [-970.0, -1865.0], [-430.0, -1216.0], [-1119.0, 434.0], [-2122.0, -698.0], [-1208.0, -1992.0], [-961.0, -1117.0], [-1205.0, 606.0], [-3796.0, -62.0], [-736.0, -2970.0], [1002.0, -187.0], [-39.0, 2425.0], [-2584.0, 1909.0], [-2109.0, 209.0], [-1262.0, -1993.0], [1116.0, 735.0], [479.0, 1771.0], [-1837.0, 611.0], [-2444.0, -783.0], [292.0, -2331.0], [240.0, 341.0], [-2441.0, 674.0], [-2020.0, -304.0], [-1010.0, 109.0], [-780.0, 446.0], [-2056.0, 11.0], [-225.0, -347.0], [-560.0, 1283.0], [-830.0, 1116.0], [-1026.0, 718.0], [-1394.0, -86.0], [0.0, -679.0], [760.0, 705.0], [-403.0, 1285.0], [-212.0, -124.0], [104.0, 319.0], [-1104.0, 738.0], [-138.0, -359.0], [70.0, 237.0], [-308.0, 106.0], [-1706.0, 724.0], [482.0, 770.0], [49.0, 1247.0], [-952.0, 386.0], [1648.0, 78.0], [742.0, 2389.0], [-2054.0, 760.0], [-676.0, -1907.0], [2442.0, -562.0], [-107.0, 2353.0], [-1513.0, 1060.0], [43.0, -640.0], [-369.0, -38.0], [1323.0, 1516.0], [251.0, 1232.0], [-897.0, 496.0], [1055.0, -574.0], [1171.0, 1082.0], [521.0, 168.0], [385.0, -561.0], [2189.0, 1216.0], [-588.0, 1410.0], [-122.0, 595.0], [1368.0, 395.0], [2031.0, 1395.0], [362.0, 11.0], [852.0, 712.0], [1207.0, 1477.0], [-244.0, 1164.0], [-210.0, -984.0], [2073.0, 143.0], [2130.0, 1077.0], [282.0, 1824.0], [-778.0, 1220.0], [1060.0, -141.0], [1561.0, 2688.0], [-371.0, 2148.0], [-299.0, 284.0], [1572.0, 1265.0], [251.0, 2036.0], [687.0, 1417.0], [714.0, 2140.0], [26.0, 2104.0], [-267.0, 1490.0], [854.0, 1286.0], [1205.0, 1887.0], [147.0, 1746.0], [176.0, 2478.0], [-301.0, 3211.0], [-73.0, 1424.0], [1652.0, 2567.0], [1005.0, 4625.0], [-731.0, 3898.0], [-1044.0, 1256.0], [106.0, 3416.0], [1408.0, 3851.0], [855.0, 3888.0], [-609.0, 5911.0], [-2721.0, 4283.0], [-1486.0, 1171.0], [928.0, 2633.0], [259.0, 5203.0], [-1860.0, 5372.0], [-1728.0, 2535.0], [123.0, 2908.0], [65.0, 3084.0], [-773.0, 3748.0], [-314.0, 3254.0], [-1211.0, 3192.0], [-1765.0, 3363.0], [-415.0, 2353.0], [236.0, 2605.0], [240.0, 3565.0], [-731.0, 3714.0], [-1426.0, 2095.0], [556.0, 902.0], [470.0, 1770.0], [-223.0, 2049.0], [-1414.0, 2931.0], [-772.0, 962.0], [472.0, 2720.0], [-939.0, 4027.0], [-2936.0, 2907.0], [-2013.0, 1189.0], [593.0, 1127.0], [1314.0, 1889.0], [-983.0, 3084.0], [-829.0, 1641.0], [-746.0, 2365.0], [-243.0, 3151.0], [-2401.0, 2072.0], [-2253.0, 926.0], [-381.0, 2147.0], [-310.0, 2381.0], [-2018.0, 2252.0], [-3039.0, 1206.0], [-537.0, 1767.0], [-2639.0, 2381.0], [-2617.0, 1176.0], [-1195.0, 1052.0], [-1043.0, 2388.0], [-2611.0, 3252.0], [-3904.0, 1824.0], [-830.0, 756.0], [-873.0, 2684.0], [-2941.0, 2587.0], [-2318.0, 2098.0], [-2363.0, 924.0], [-2085.0, 64.0], [-842.0, 1620.0], [-2995.0, 3982.0], [-4560.0, 1930.0], [-3712.0, 993.0], [-3272.0, 1912.0], [-3693.0, 1818.0], [-3284.0, 1858.0], [-3184.0, 1607.0], [-4310.0, 1765.0], [-3951.0, 1535.0], [-4215.0, 2030.0], [-4931.0, 1372.0], [-3975.0, 1757.0], [-4075.0, 1456.0], [-4575.0, 56.0], [-3643.0, 1030.0], [-4702.0, 1519.0], [-4331.0, 1640.0], [-4796.0, 441.0], [-5487.0, 703.0], [-4475.0, -1006.0], [-2542.0, -256.0], [-4598.0, 2409.0], [-5032.0, 834.0], [-5966.0, -412.0], [-4088.0, -424.0], [-4109.0, -1344.0], [-3318.0, 458.0], [-4346.0, 445.0], [-5193.0, -469.0], [-3586.0, -325.0], [-3495.0, -416.0], [-4693.0, -873.0], [-3821.0, -117.0], [-3611.0, -727.0], [-3470.0, -1453.0], [-3275.0, -2.0], [-3571.0, -499.0], [-3601.0, -1394.0], [-2701.0, -846.0], [-4084.0, -404.0], [-3785.0, -982.0], [-3447.0, -960.0], [-3309.0, -765.0], [-5094.0, -842.0], [-3378.0, -1431.0], [-2960.0, -1437.0], [-2210.0, -428.0], [-3458.0, -908.0], [-2621.0, -1812.0], [-1846.0, -1058.0], [-2499.0, -740.0], [-3495.0, -1617.0], [-1324.0, -2649.0], [-1895.0, -1171.0], [-1685.0, -613.0], [-2746.0, -1712.0], [-1519.0, -2092.0], [-1551.0, -2033.0], [-2109.0, -1654.0], [-2169.0, -1378.0], [-2891.0, -2078.0], [-1956.0, -2684.0], [-1121.0, -1554.0], [-1558.0, -2605.0], [-1536.0, -2088.0], [-1642.0, -1556.0], [-723.0, -2045.0], [-552.0, -1933.0], [-552.0, -1969.0], [-672.0, -1042.0], [295.0, -1308.0], [-428.0, -1742.0], [-574.0, -1828.0], [-208.0, -1071.0], [-15.0, -1312.0], [-730.0, -1409.0], [-25.0, -1734.0], [22.0, -1425.0], [-680.0, -370.0], [-890.0, -1468.0], [56.0, -3111.0], [755.0, -2323.0], [144.0, -1812.0], [-1369.0, -1778.0], [646.0, -2776.0], [360.0, -1434.0], [91.0, -1682.0], [-750.0, -2005.0], [216.0, -739.0], [897.0, -1021.0], [88.0, -1977.0], [245.0, -2123.0], [-252.0, -1464.0], [321.0, -1405.0], [921.0, -1723.0], [1219.0, -1639.0], [840.0, -1210.0], [847.0, -249.0], [-179.0, -1988.0], [1034.0, -2605.0], [1074.0, -1394.0], [845.0, -776.0], [814.0, -1346.0], [764.0, -1364.0], [1054.0, -1787.0], [472.0, -1746.0], [1455.0, -814.0], [1206.0, -986.0], [901.0, -819.0], [693.0, -936.0], [2159.0, 817.0], [1494.0, -871.0], [1748.0, -585.0], [2421.0, 229.0], [1074.0, -1017.0], [724.0, -1717.0], [2283.0, -1362.0], [2456.0, -806.0], [896.0, -681.0], [1753.0, -774.0], [1521.0, -846.0], [1792.0, -942.0], [2497.0, -1498.0], [2176.0, -1177.0], [1468.0, -789.0], [659.0, -1524.0], [2960.0, -1901.0], [1535.0, -1746.0], [2073.0, -1346.0], [1357.0, -585.0], [1849.0, -2105.0], [1758.0, -1497.0], [2027.0, -1732.0], [2629.0, -985.0], [2310.0, -1377.0], [2337.0, -328.0], [2143.0, -214.0], [2139.0, -858.0], [2389.0, -366.0], [2567.0, -886.0], [1640.0, -589.0], [1851.0, -1348.0], [2509.0, -603.0], [2834.0, -2175.0], [2633.0, -1545.0], [1820.0, -1678.0], [2161.0, -2020.0], [3203.0, -1850.0], [3372.0, -1885.0], [2254.0, -1753.0], [2427.0, -1580.0], [2958.0, -1719.0], [3328.0, -1918.0], [3315.0, -1252.0], [1380.0, 115.0], [2707.0, -1140.0], [2522.0, -579.0], [3155.0, -1422.0], [1844.0, -280.0], [1252.0, -539.0], [2691.0, -683.0], [2835.0, 263.0], [2408.0, -225.0], [1502.0, -262.0], [3525.0, -213.0], [3112.0, -1060.0], [2494.0, -729.0], [2718.0, -935.0], [2352.0, -634.0], [3371.0, -1314.0], [3038.0, -317.0], [2298.0, -646.0], [2438.0, -530.0], [2323.0, 21.0], [2072.0, -680.0], [1799.0, -379.0], [2721.0, -670.0], [3159.0, -409.0], [3183.0, 239.0], [2524.0, -793.0], [1871.0, -374.0], [2203.0, 481.0], [1801.0, -149.0], [1501.0, 864.0], [1909.0, -234.0], [2657.0, 108.0], [2027.0, 348.0], [2795.0, 672.0], [1689.0, 1325.0], [1508.0, 467.0], [2412.0, 631.0], [2476.0, -791.0], [1934.0, -329.0], [3038.0, 257.0], [2280.0, -131.0], [2411.0, 397.0], [1800.0, -182.0], [2844.0, 174.0], [1789.0, 17.0], [2448.0, 332.0], [3170.0, 630.0], [2464.0, 772.0], [3072.0, 1561.0], [1779.0, 268.0], [2762.0, 145.0], [2741.0, -93.0], [2591.0, 359.0], [2703.0, 33.0], [2697.0, 712.0], [1922.0, 652.0], [2021.0, 476.0], [2325.0, 70.0], [3066.0, 1052.0], [2879.0, -401.0], [3213.0, 158.0], [3273.0, -210.0], [2806.0, -60.0], [3342.0, 844.0], [2861.0, 786.0], [2731.0, -65.0], [3192.0, 1349.0], [2268.0, 501.0], [2811.0, 770.0], [2745.0, 872.0], [2923.0, 602.0], [2592.0, 1057.0], [1981.0, 224.0], [2776.0, 681.0], [2391.0, -765.0], [2114.0, 1137.0], [1162.0, 457.0], [2420.0, 549.0], [2429.0, 1260.0], [2760.0, 1647.0], [1763.0, 918.0], [2887.0, -237.0], [1931.0, 1289.0], [2228.0, 1366.0], [2177.0, 445.0], [2862.0, 210.0], [3074.0, 913.0], [2074.0, 521.0], [2988.0, 1069.0], [3781.0, 876.0], [4167.0, 148.0], [3346.0, 56.0], [3045.0, 934.0], [3199.0, 923.0], [3036.0, 1233.0], [4352.0, 583.0], [2822.0, 972.0], [3051.0, 1344.0], [2975.0, 703.0], [3066.0, 1846.0], [1897.0, 1089.0], [1703.0, 1628.0], [2221.0, 1944.0], [1808.0, 1318.0], [1382.0, 811.0], [2130.0, 1001.0], [2883.0, 1361.0], [1604.0, 1132.0], [1358.0, 788.0], [1744.0, 1314.0], [964.0, 1385.0], [986.0, 1169.0], [98.0, 376.0], [1241.0, 1242.0], [785.0, 1262.0], [842.0, 1388.0], [-301.0, 1842.0], [778.0, 742.0], [9.0, 1399.0], [-45.0, 525.0], [-43.0, 613.0], [323.0, 206.0], [440.0, 1546.0], [-515.0, 996.0], [-238.0, 524.0], [-195.0, 111.0], [-7.0, 1106.0], [371.0, 941.0], [-355.0, 87.0], [-278.0, 236.0], [-472.0, 1460.0], [-410.0, 746.0]]

def actual_data():
    ts = map(lambda x: x[0] + 1j * x[1], points)

    newFigure()
    plotC(ts)
    
    ft = numpy.fft.fft(ts)
    
    newFigure()
    plotC(ft)
