#-*-coding:utf-8-*-

import arcpy, string

arcpy.env.workspace = r"C:\EsriTraining"
arcpy.env.overwriteOutput = True

arcpy.CreateFeatureclass_management(r"C:\EsriTraining", "TrailsCoords.shp", 'Polyline')
with arcpy.da.InsertCursor(r'C:\EsriTraining\TrailsCoords.shp', ['ID','SHAPE@']) as cursor:

    txt = open(r'C:\EsriTraining\{}'.format('TrailsCoords.txt'), "r")

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
