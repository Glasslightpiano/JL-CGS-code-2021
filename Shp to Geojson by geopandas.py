# Turn shp to geojson.
# Install geopandas modules.
# "For" loop.
# Created on: 2021-11-16 10:55:37
# ------------------------------------------------------------------------------------------------

# Import modules
import geopandas
import os

# Set path
path = "D:/ArcMap test/State/Stuttgart/"
export = "D:/ArcMap test/To geojson try/"

# Select all .shp file by "for" loop
file = os.listdir(path)
for shpfile in file:
    if shpfile.endswith(".shp"):
        input_layer = path + shpfile
        out_layer = export + shpfile[:-4] + ".geojson"

        # Turn .shp to .geojson
        myshpfile = geopandas.read_file(input_layer)
        myshpfile.to_file(out_layer, encoding='utf-8', driver='GeoJSON')

print("Done!")