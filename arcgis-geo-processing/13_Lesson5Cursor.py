#-*-coding:utf-8-*-
#한글


import arcpy
try:
    arcpy.env.workspace = r"C:\EsriTraining\PYTH\Cursors\SanDiego.gdb"

    #arcpy.SearchCursor #이전 버전
    #arcpy.da.SearchCursor #현재 버전

    #with구문은 소스구간을 지나면 메모리에서 자동 릴리즈 됨
    #cursor arcpy.da.SearchCursor("Parcle") #da -> dataAccess
    #del cursor #del이 필요 없어짐

    #데이터 읽기
    with arcpy.da.SearchCursor("MajorAttractions", ["OBJECTID", "NAME", "SHAPE@XY", "SHAPE@X", "SHAPE@JSON", "SHAPE@"]) as cursor:
        for row in cursor:
            print str(row[0]) + " NAME : " + row[1] + " X,Y Coord : " + str(row[2]) + " X Coord : " + str(row[3])

    #데이터 업데이트
    with arcpy.da.UpdateCursor("MajorAttractions", ["OBJECTID", "NAME", "SHAPE@X", "SHAPE@"]) as cursor:
        for row in cursor:
            geom = row[3]
            row[1] = "AAAAA"
            cursor.updateRow(row)
            #cursor.deleteRow()

    #데이터 추가
    with arcpy.da.InsertCursor("MajorAttractions", ["OBJECTID", "NAME",  "SHAPE@"]) as cursor:
        for row in cursor:
            print row["1", "saaa", geom]
            cursor.insertRow(row)

except:
    arcpy.GetMessage(2)