from netCDF4 import Dataset
import numpy as np
from data import *
import sys

ncv = Dataset(sys.argv[1])
data = ncv.variables
# ncv.close()
print(data)
