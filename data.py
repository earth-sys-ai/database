# database manegment
import psycopg2
import sys

con = psycopg2.connect(
    database = "earthsysai",
    user = "admin",
    password = sys.argv[1],
    host = "mbstorage.us.to",
    port = 5432
)
cur = con.cursor()

# parse list to json
def parseList(l, q):
    if (q):
        return ("[" + ",".join(str(x[0]) for x in l) + "]")
    else:
        return ("[" + ",".join(x[0].replace("(", "[").replace(")", "]") for x in l) + "]")
        

# get location data
def getData(lat, lng):
    cur.execute("select data from surge where location ~= point(" + lat + "," + lng + ");")
    return ("{\"data\":" + parseList(cur.fetchall(), True) + "}")

# clear location data
def clearData(lat, lng):
    cur.execute("delete from surge where location ~= point(" + lat + "," + lng + ");")
    con.commit()

# add data for location
def addData(lat, lng, add):
    cur.execute("insert into surge values ((point(" + lat + ", " + lng + ")), '" + add + "');")
    con.commit()

# list locations where data exists
def listData(lat, lng, rad):
    cur.execute("select location from surge where location <@> Point(" + lat + ", " + lng + ") < " + rad + ";")
    points = cur.fetchall()
    cur.execute("select data from surge where location <@> Point(" + lat + ", " + lng + ") < " + rad + ";")
    vals = cur.fetchall()

    return ("{\"points\":" + parseList(points, False) + ",\"values\":" + parseList(vals, True) + "}")
