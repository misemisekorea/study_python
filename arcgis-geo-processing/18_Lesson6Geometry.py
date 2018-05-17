import arcpy
###############################################################
#feature copy, object length
arcpy.env.workspace = r"C:\EsriTraining\PYTH\Geometry_objects\SanDiego.gdb"

geometry = arcpy.Geometry()
geomList = arcpy.CopyFeatures_management("Railroads", geometry)

length = 0
for geom in geomList:
    length += geom.length

print "Total length in miles : {0}".format(round(length / 5280, 2))

###############################################################
#create the multipart polyline geometry object
partOne = arcpy.Array([arcpy.Point(5997624.6225,2069868.8208),
                        arcpy.Point(5997674.94199,2069833.81741)])
partTwo = arcpy.Array([arcpy.Point(5997616.44497,2069862.32774),
                        arcpy.Point(5997670.57373,2069824.67456)])

ary = arcpy.Array([partOne, partTwo])
multiPartPolyline = arcpy.Polyline(ary)

print multiPartPolyline.partCount


###############################################################
#create the multipart polygon geometry object
intRingAry = arcpy.Array([arcpy.Point(7,10),arcpy.Point(7,9),arcpy.Point(8,9),arcpy.Point(8,10)])
extRingAry = arcpy.Array([arcpy.Point(9,11),arcpy.Point(9,8),arcpy.Point(6,8),arcpy.Point(6,11)])
extRingAry2 = arcpy.Array([arcpy.Point(2,10),arcpy.Point(3,8),arcpy.Point(1,8)])

array = arcpy.Array([extRingAry, intRingAry, extRingAry2])
poly = arcpy.Polygon(array)
print "Parts: {0}, points: {1}".format(poly.partCount, poly.pointCount)


###############################################################
#writing geometries with an arcpy.da.InsertCursor
#parameter(featClass)
cursor = arcpy.da.InsertCuror(featClass, "SHAPE@")
ary = arcpy.Array([arcpy.Point(9,11),arcpy.Point(9,8),arcpy.Point(6,8),arcpy.Point(6,11)])
polygon = arcpy.Polygon(ary)
cursor.insertRow([polygon])
del cursor

###############################################################
#Updating geometries with an arcpy.da.UpdateCursor
#parameter(featClass)
exp = """ "name" = 'Balboa Park' """
cursor = arcpy.da.UpdateCursor(featClass, "SHAPE@XY", exp)
for row in cursor:
    row[0] = arcpy.Point(6285430.0,1844965.66)
    cursor.updateRow(row)
del cursor

###############################################################
#Reading geometries with a arcpy.da.SearchCursor
for row in arcpy.da.SearchCursor("Parks", ["SHAPE@AREA", "NAME"]):
    area = row[0]
    acreage = area / 43560
    print("{0} Acres: {1}, Area: {2}".format(row[1],acreage,row[0]))







###############################################################
###############################################################
###############################################################