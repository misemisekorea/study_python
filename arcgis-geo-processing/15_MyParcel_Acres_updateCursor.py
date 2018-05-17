#-*-coding:utf-8-*-
"""
#Parcel dataFeature에 ACRES 필드를 생성하고 ACRES, SHAPE를 가져오고 ACRES에 area / 43560 를 업데이트(updateRow)
"""

# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PYTH\Cursors\Corvallis.gdb" #필지 Data

# Add a new field named ACRES to the Parcel feature class
#Syntax: arcpy.AddField_management (in_table, field_name, field_type, {field_precision},
#                                   {field_scale}, {field_length},
#                                   {field_alias}, {field_is_nullable},
#                                   {field_is_required}, {field_domain})
arcpy.AddField_management ("Parcel", "ACRES", "Double")# in_table, field_name, field_type

# Update ACRES field.  Use SHAPE@ token and calculate acres
# The conversion from area in square feet to acres is:
# area value / 43560
# In the code below, a geometry object is returned from row[0]
# The area property is obtained from the SHAPE@AREA token, converted to acres
# and then assigned to the "ACRES" index position in the row list object.
with arcpy.da.UpdateCursor("Parcel", ["SHAPE@AREA", "ACRES"]) as cursor:
    for row in cursor:
        geom = row[0] # Obtain the shape geometry from the SHAPE@ token
        row[1] = geom / 43560 # Access the area value from the geometry shape and convert to acres
        cursor.updateRow(row)

print("Script completed")