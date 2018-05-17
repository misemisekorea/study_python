# -*- coding: utf-8 -*-
import arcpy


arcpy.env.workspace = r'C:\EsriTraining\PYTH\Running_scripts\Corvallis.gdb'#작업경로 설정
arcpy.env.overwriteOutput = True#덮어쓰기 세팅

#Feature class에서 정보 가져오기
fc = arcpy.Describe("Schools")

print fc.baseName #공통
print fc.shapeType #Point
print fc.OIDFieldName #OBJECTID
print fc.datasetType #FeatureClass


#공통 속성정보 가져오기

arcpy.env.workspace = r"C:\EsriTraining\PYTH\Describe\Corvallis.gdb"#작업경로 설정
desc = arcpy.Describe("Building")
fldList = desc.fields # ["OBJECTID", "TYPE", "Shape", "Shape_Area"]

for fld in fldList:
    print "{} : {}".format(fld.baseName, fld.type)




