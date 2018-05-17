######################################################################
## Populate_XY.py
## Purpose:  Work with an arcpy.da InsertCursor to populate new features
##
######################################################################
#-*-coding:utf-8-*-
"""
FeatureClass(SanDiego.gdb > MajorAttractionsWGS84)에 rows(Name,Point) 추가(insertRow)
"""
# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PYTH\Cursors\SanDiego.gdb"

# Create a list of name and coordinate pairs.
rowValues = [["The Haunted Hotel", (-117.161, 32.712)], ["The New Children's Museum", (-117.165, 32.711)],
             ["San Diego Library", (-117.154, 32.709)], ["Pantoja Park", (-117.168, 32.713)]]

# Create an arcpy.da.InsertCursor on MajorAttractions
iCur = arcpy.da.InsertCursor("MajorAttractionsWGS84", ["NAME", "SHAPE@XY"])

for row in rowValues:
    iCur.insertRow(row)

# Delete the cursor to close the cursor and release the exclusive lock
del iCur

print("Script completed")
