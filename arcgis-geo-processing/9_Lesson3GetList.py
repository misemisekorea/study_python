# -*- coding: utf-8 -*-
"""
주석 처리
주석 처리
"""
######################################
#Feature 가져오기
import arcpy
arcpy.env.workspace = r'C:\EsriTraining\ARC3\Prepare\CountyData'

shp_list = arcpy.ListFeatureClasses()

for shp in shp_list:
    print shp

#C로 시작하는 Feature 가져오기
shp_list = arcpy.ListFeatureClasses("C*")

for shp in shp_list:
    print shp

#Poligon 가져오기
shp_list = arcpy.ListFeatureClasses("*", "Polygon")

for shp in shp_list:
    print shp

#Poliline 가져오기
shp_list = arcpy.ListFeatureClasses("*", "Polyline")

for shp in shp_list:
    print shp

#fields 가져오기
shp_list = arcpy.ListFeatureClasses("CCPA.shp") #["CCPA.shp"] getString
shp_list = arcpy.ListFields("CCPA.shp") #[field, field, field] getObject

for shp in shp_list:
    print shp.name + " , " + shp.type

######################################
#최상위 폴더에서 모든 혹은 특정 데이터 가져오기 (workspace, datatype, type)
import arcpy, os

workspace = r'C:\EsriTraining'
fcList = []

walk = arcpy.da.Walk(workspace, datatype="FeatureClass", type="Polygon")

for dirpath, dirname, filenames in walk:
    for filename in filenames:
        fcList.append(os.path.join(dirpath, filename))

print fcList







