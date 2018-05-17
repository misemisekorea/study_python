#-*- coding: utf-8 -*-

import arcpy
try:
    arcpy.env.workspace = "C:/EsriTraining/PYTH/Selections/SanDiego.gdb"#file geodatabase
    #arcpy.env.workspace = "C:/EsriTraining/PYTH/Selections/SanDiego.mdb"#personal geodatabase
    #arcpy.env.workspace = "C:/EsriTraining/PYTH/Selections/SanDiego"    #shapefile

    newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"TYPE")
    newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"ESTAB")

    print(newField1)
    print(newField2)
    # TYPE = 'Maritime'
    # [TYPE] = 'Maritime'
    # "TYPE" = 'Maritime'

    # ESTAB > 0 AND ESTAB < 1956
    # [ESTAB] > 0 AND [ESTAB] < 1956
    # "ESTAB" > 0 AND "ESTAB" < 1956


    maritimeSQLExp = newField1 + " = " + "'Maritime'"
    historicSQLExp = newField2 + " > 0 and " + newField2 + " < 1956"

    arcpy.MakeFeatureLayer_management("Climate", "MaritimeLyr", maritimeSQLExp) #TYPE = Maritime
    arcpy.MakeFeatureLayer_management("MajorAttractions", "HistoricLyr",
                                        historicSQLExp) #ESTAB > 0 AND ESTAB < 1956

    arcpy.SelectLayerByLocation_management("HistoricLyr", "COMPLETELY_WITHIN",
                                            "MaritimeLyr", "", "NEW_SELECTION")#HistoricLyr(point), MaritimeLyr(polygon)

    featCount = arcpy.GetCount_management("HistoricLyr") #MaritimeLyr에 포함된 HistoricLyr를 선택
    print ("Number of historic features selected: {}".format(featCount)) #갯수 출력

except:
    print arcpy.GetMessages(2)