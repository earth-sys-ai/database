# database manegment
import psycopg2

con = psycopg2.connect(
    database = "earthsysai",
    user = "admin",
    password = "earthsysai",
    host = "mbstorage.us.to",
    port = 5432
)
cur = con.cursor()

# parse list to json
def parseList(l, q):
    if (q):
        return ("[" + ",".join(("\"" + x[0].replace("(", "[").replace(")", "]") + "\"") for x in l) + "]")
    else:
        return ("[" + ",".join(x[0].replace("(", "[").replace(")", "]") for x in l) + "]")

# get location data
def getData(lat, lng):
    cur.execute("select data from test where location ~= point(" + lat + "," + lng + ");")
    return ("{\"data\":" + parseList(cur.fetchall(), True) + "}")

# clear location data
def clearData(lat, lng):
    cur.execute("delete from test where location ~= point(" + lat + "," + lng + ");")
    con.commit()

# add data for location
def addData(lat, lng, add):
    cur.execute("insert into test values ((point(" + lat + ", " + lng + ")), '" + add + "');")
    con.commit()

# list locations where data exists
def listData():
    cur.execute("select location from test;")
    return ("{\"points\":" + parseList(cur.fetchall(), False) + "}")
