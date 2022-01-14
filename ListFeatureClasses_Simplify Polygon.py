# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ListDatasets.py
# SimplifyPolygon.py
# Created on: 2021-02-19 10:46:51.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
import arcpy.cartography as CA
import os

# Set input path & output path
arcpy.env.workspace = "D:\\CGSprogram\\History_singal_9\\"
simplify_path = "D:\\CGSprogram\\History_simplifypolygon_9\\"

# Until "Workfile" is "Get all Shp. file under this path."
# After "in_features" is "Simplify Polygon."
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        Workfile = os.path.join(arcpy.env.workspace, ds, fc)
        in_feature = Workfile
        out_feature = simplify_path + fc
        if arcpy.Exists(in_feature):
            CA.SimplifyPolygon(in_feature, out_feature, "POINT_REMOVE", 10, 0, "NO_CHECK", "KEEP_COLLAPSED_POINTS")
            print fc + " is completed Simplify Polygon."

print "Finished."