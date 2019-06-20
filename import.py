# imports netcdf file to database
# takes database password and file location

from netCDF4 import Dataset
import numpy as np
import sys
from contourVector import vectorize

ncv = Dataset(sys.argv[2])
cdf = ncv.variables

# variables to array of polygons
def getData(cdf):
    lat = cdf["y"][:]
    lon = cdf["x"][:]
    elems = cdf['element'][:,:]-1
    data = cdf['zeta_max'][:]
    return vectorize(lat, lon, elems, data, sys.argv[3], (len(sys.argv) == 5));


# prints 2d data
def printData(data):
    lat = data[0]
    lon = data[1]
    elems = data[2]
    for i in range(len(lat)):
        curLat = lat[i]
        curLon = lon[i]
        curelems = elems[i]
        print('(' + repr(curLat) + ', ' + repr(curLon) + '): ' + repr(curelems))


# stores 2d data in database
# currently does not work
def storeData(data):
    con = psycopg2.connect(
        database = "earthsysai",
        user = "admin",
        password = sys.argv[1],
        host = "mbstorage.us.to",
        port = 5432
    )
    cur = con.cursor()

    lat = data[0]
    lon = data[1]
    elems = data[2]

    leng = len(lat)
    for i in range(leng):
        curLat = lat[i]
        curLon = lon[i]
        curelems = elems[i]
        addData(curLat.astype(str), curLon.astype(str), curelems.astype(str))
        print(str(i) + '/' + str(leng))
    
data = getData(cdf)
#print(data)
#print(len(getData(cdf)[0]))