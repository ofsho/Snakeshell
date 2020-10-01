import os
import sys
import mmap

platform = sys.platform

exists = True

def sample(i):
    i += 1
    return i