#-*-coding:utf-8-*-
import arcpy
arcpy.env.workspace = r'C:\Users\Administrator\Documents\ArcGIS\Default.gdb'


grid_area_muan = "grid_area_muan"
spotheight_muan = "spotheight_muan"




#데이터 읽기
with arcpy.da.SearchCursor(grid_area_muan, ["OBJECTID", "SHAPE@XY", "SHAPE@X", "SHAPE@JSON", "SHAPE@"]) as cursor:
    for row in cursor:
        print "OBJECTID : " + str(row[0]) + " X,Y Coord : " + str(row[1]) + " X Coord : " + str(row[2])
        arcpy.SelectLayerByLocation_management(spotheight_muan, "INTERSECT", row[4], "", "NEW_SELECTION", "")

