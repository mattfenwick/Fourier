stcommand = '''
java -jar ConnjurST.jar -st nmrpipe -sf ../Documents/workspace/CJRTestData/nmrpipe.d/pipe1D_folder/1Dspectrum.dat -dt tabular -df out.txt
'''

lines = data.split('\n')

import re
myre = re.compile('(\d+)\s+([RI])\s+(\\-?[0-9\\.,]+)')

points = [[None, None] for x in range(512)]

for line in lines:
   (ix, q, num) = myre.search(line).groups()
   ix1, num1 = int(ix), float(num.replace(',', ''))
   y = None
   if q == 'R':
     y = 0
   elif q == 'I':
     y = 1
   if y is None:
     raise ValueError('invalid quadrature: ' + q)
   if points[ix1][y] is not None:
     raise ValueError('duplicate index: ' + str([ix1, y1]))
   points[ix1][y] = num1
