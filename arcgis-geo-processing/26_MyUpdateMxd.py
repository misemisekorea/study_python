#-*-coding:utf-8-*-
######################################################################
## UpdateMxd.py
##
## results script without pseudocode
######################################################################

## Step 1
import arcpy.mapping as MAP
import arcpy.da as DA

mxd = MAP.MapDocument(r"C:\EsriTraining\PYTH\Map_production\CorvallisMeters.mxd")
df = MAP.ListDataFrames(mxd)[0]

## Step 2
updateLayer = MAP.ListLayers(df, "ParkingMeters")[0]
sourceLayer = MAP.Layer(r"C:\EsriTraining\PYTH\Map_production\ParkingMeters.lyr")
MAP.UpdateLayer(df, updateLayer, sourceLayer, True)# updateLayer to sourceLayer

addLayer = MAP.Layer(r"C:\EsriTraining\PYTH\Map_production\Schools.lyr")
MAP.AddLayer(df, addLayer)

refLayer = MAP.ListLayers(df, "Schools")[0]

## This is the tricky step.  The order of the arguments appears to be backwards.
MAP.MoveLayer(df, refLayer, updateLayer, "BEFORE")#Schools레이어를 ParkingMeters 레이어 밑으로 이동

## Step 3
mxd.title = "Corvallis Meters Map"#Central Park Parking Meters -> Corvallis Meters Map
elemList = MAP.ListLayoutElements(mxd, "TEXT_ELEMENT")

#LayoutView의 레이아웃객체리스트를 가져와서
#Corvallis Meters -> Corvallis Parking Meters Inventory Report 로 변경
for elem in elemList:
    if elem.name == "Corvallis Meters":
        elem.text = "Corvallis Parking Meters Inventory Report"

mxd.saveACopy(r"C:\EsriTraining\PYTH\Map_production\CorvallisMeters_ks.mxd")
del mxd