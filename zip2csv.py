#!/usr/bin/env python

import numpy as np
import sys

array = np.fromfile(sys.argv[1], dtype=np.int8)

print(array)

np.savetxt(sys.argv[1] + '.csv', array, delimiter=",", fmt='%d')
