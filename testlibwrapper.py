import ctypes
import ctypes.util

#
# Locate the library
#
lib = ctypes.util.find_library('testlib')
#
# Load the library
#
testlib = ctypes.CDLL(lib)
testlib.myprint()
