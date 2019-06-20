# vectorizes array of values into a array of polygons
# each element in the output array contains two elements:
# an array of polygons, and a value
# each polygon contains an array of coordinates


import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

# returns an array of polygons and values
def genPoly(cs, levels):
    outp = []
    for i, collection in enumerate(cs.collections):
        poly = []
        for path in collection.get_paths():
            verts = path.to_polygons()
            for v in verts:
                poly.append(v)
        outp.append([poly, levels[i]])
    return outp


# takes raster points and generates a vector contour
def vectorize(lat, lon, elems, data, res, show):
    MinVal    = np.min(data) 
    MaxVal    = np.max(data)
    levels = np.linspace(MinVal, MaxVal, num=res)
    triangles = tri.Triangulation(lon,lat, triangles=elems)
    contour = plt.tricontourf(triangles, data, levels=levels ,extend='max')
    if (show):
        plt.show()
    return genPoly(contour, levels)
