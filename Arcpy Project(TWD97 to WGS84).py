# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# ListDatasets.py
# Project_management.py
# Turn shp coordinate by for loop
# In this case is TWD97 turn to WGS84
# Create on: 2023-01-11 11:03:29
# -----------------------------------------------------------------------

# Import arcpy module
import arcpy
import os

# Set input path & output path
arcpy.env.workspace = "D:\\CGS\\TWD97\\History\\"
coordinateTurnOut = "D:\\CGS\\WGS84\\History\\"

# Until "workFile" is "Get all Shp. file under this path."
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for countyName in arcpy.ListFeatureClasses(feature_dataset=ds):
        workFile = os.path.join(arcpy.env.workspace, ds, countyName)
        inFeature = workFile                            # Set input path
        outFeature = coordinateTurnOut + countyName     # Set output path
        outCs = arcpy.SpatialReference('WGS 1984')      # Set output coordinate system

        # Run Project_management
        if arcpy.Exists(inFeature):
            arcpy.Project_management(inFeature, outFeature, outCs)
            print (countyName + " has turned to WGS84.")

print ("All Finish!")
