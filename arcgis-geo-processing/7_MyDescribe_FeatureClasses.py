# -*- coding: utf-8 -*-

import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PYTH\Describe\Corvallis.gdb"
arcpy.env.overwriteOutput = True

fc_list = arcpy.ListFeatureClasses()#FeatureClass 목록을 가져온다.
for name in fc_list:
    desc = arcpy.Describe(name)
    featCount = arcpy.GetCount_management(name)
    print ("Name: {} Shape: {} SR: {} Count: {}".format(
        desc.name, desc.shapeType, desc.spatialReference.name, featCount))

print ("Script completed")