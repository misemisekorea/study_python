# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PYTH\Describe\Tahoe\All"
arcpy.env.overwriteOutput = True

desc = arcpy.Describe(r"C:\EsriTraining\PYTH\Describe\Tahoe\Emer\erelev")
rasExtent = desc.extent
ras_List = arcpy.ListRasters()#Raster 리스트를 가져온다.

for name in ras_List:
    arcpy.Clip_management(name, str(rasExtent), "{}_clip".format(name))

#Alternate way to acces the Clip_management geoprocessing tool is to
# specify the toolbox alias and them the name in the form of:
# arcpy.<toolbox alias>.<toolname>()
# Alternate code for line 19 above is:
#arcpy.management.Clip(name, str(rasExtent), "{}_clip".format(name))

print ("Script completed")

