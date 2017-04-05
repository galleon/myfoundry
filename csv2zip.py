#!/usr/bin/env python

import numpy as np
import sys

array = np.genfromtxt(sys.argv[1], dtype=np.int8, delimiter=",")

print(array.dtype)

array.tofile(sys.argv[1] + '.zip')
