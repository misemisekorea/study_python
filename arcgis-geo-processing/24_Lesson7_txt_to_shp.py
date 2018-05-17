#-*-coding:utf-8-*-

import arcpy, string
######################################################################################
#Run>Command Line Parameter (1 2 3 4)
#'C:\EsriTraining\TrailsCoords.txt' "C:\EsriTraining" "TrailsCoords2.shp" 'Polyline'
######################################################################################
sourceData = arcpy.GetParameterAsText(0)
outputFCPath = arcpy.GetParameterAsText(1)
outputFC = arcpy.GetParameterAsText(2)
FcType = arcpy.GetParameterAsText(3)

arcpy.env.workspace = r"C:\EsriTraining"
arcpy.env.overwriteOutput = True

arcpy.CreateFeatureclass_management(outputFCPath, outputFC, FcType)
with arcpy.da.InsertCursor(r'C:\EsriTraining\TrailsCoords.shp', ['ID','SHAPE@']) as cursor:

    txtFile = open(sourceData, "r")

    lines = txt.readlines()
    pnt = arcpy.Point()
    lineArray = arcpy.Array()
    tmpId = -1

    for line in lines:
        values = line.replace('\n','').split(' ')
        pnt.ID = values[0]
        pnt.x = values[1]
        pnt.y = values[2]
        print("values : " + values[0] + " , " + values[1] + " , " + values[2])


        if tmpId == -1:
            tmpId = pnt.ID
        if tmpId != pnt.ID:
            print ("lineArray : " + str(len(lineArray)))
            lineFeature = arcpy.Polyline(lineArray)
            print lineFeature.pointCount
            cursor.insertRow((tmpId, lineFeature))
            lineArray.removeAll()

        tmpId = pnt.ID
        lineArray.add(arcpy.Point(pnt.x, pnt.y))

    lineFeature = arcpy.Polyline(lineArray) #마지막 Polyline Add
    cursor.insertRow((tmpId, lineFeature))

    del txt

print("script completed")
