# imports netcdf file to database
# takes database password and file location

from netCDF4 import Dataset
import numpy as np
from data import *
import sys
from data import *

ncv = Dataset(sys.argv[2])
cdf = ncv.variables


# variables to 2d array of values
def getData(cdf):
    lat = np.array(cdf['y'][:])
    lon = np.array(cdf['x'][:])
    surge = np.array(cdf['surge'][:])
    return [lat, lon, surge];


# prints 2d data
def printData(data):
    lat = data[0]
    lon = data[1]
    surge = data[2]

    for i in range(len(lat)):
        curLat = lat[i]
        curLon = lon[i]
        curSurge = surge[i]
        print('(' + repr(curLat) + ', ' + repr(curLon) + '): ' + repr(curSurge))


# stores 2d data in database
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
    surge = data[2]

    leng = len(lat)
    for i in range(leng):
        curLat = lat[i]
        curLon = lon[i]
        curSurge = surge[i]
        addData(curLat.astype(str), curLon.astype(str), curSurge.astype(str))
        print(str(i) + '/' + str(leng))
    
storeData(getData(cdf))
#print(len(getData(cdf)[0]))