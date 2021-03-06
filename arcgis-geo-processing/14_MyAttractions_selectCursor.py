######################################################################
## MyAttractions.py
## Purpose:  Use the arcpy.da.SearchCursor to obtian field values
##          Print a three line address style listing of the data
##
######################################################################

# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = "C:/EsriTraining/PYTH/Cursors/SanDiego.gdb"

# Create a feature layer on MajorAttractions feature class
# Syntax: arcpy.MakeFeatureLayer_management (in_features, out_layer, {where_clause},
#                                           {workspace}, {field_info})
arcpy.MakeFeatureLayer_management("MajorAttractions", "AttractionsLyr")

# Syntax: arcpy.da.SearchCursor (in_table, field_names, {where_clause},
#                               {spatial_reference}, {explode_to_points}, {sql_clause})

with arcpy.da.SearchCursor("MajorAttractions", ["NAME", "ADDR", "CITYNM", "ZIP"]) as cursor:
    for row in cursor:
        print ("{0}\n{1}\n{2}, CA {3}\n".format(row[0], row[1], row[2], row[3]))


in_memory_buffer10000 = arcpy.Buffer_analysis(arcpy.PointGeometry(arcpy.Point(123,123)), "in_memory\Buffer10000", "10000 feet")#(input,output,distance)
print(in_memory_buffer10000)