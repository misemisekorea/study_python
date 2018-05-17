#-*- coding: utf-8 -*-
## Point 는 1000 feet로 버퍼
## Polyline 은 500 feet로 버퍼
## Polygon 은 -750 feet로 버퍼

import arcpy
arcpy.env.workspace = r"C:/EsriTraining/PYTH/Automate/SanDiego.gdb"

fc_list = arcpy.ListFeatureClasses()
for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType == "Point":
        buffDist = '1000 feet'
    elif desc.shapeType == "Polyline":
        buffDist = '500 feet'
    elif desc.shapeType == "Polygon":
        buffDist = '-750 feet'
    arcpy.Buffer_analysis(in_features = featClass,
                    out_feature_class = featClass + "_Buff",
                    buffer_distance_or_field = buffDist)

print ("Script completed")
