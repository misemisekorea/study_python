#-*- coding: utf-8 -*-
## 텍스트 파일에 Describe를 write(Name, Type, length)
import arcpy

enviro = r"C:/EsriTraining/PYTH/Automate/"
arcpy.env.workspace = enviro +"{}".format("SanDiego.gdb")
field_list = arcpy.ListFields("MajorAttractions")

txtFile = open(enviro +"{}".format("Majorattractions.txt"),"w")
txtFile.write("MajorAttractions field information" + "\n")
txtFile.write("-------------------------------------" + "\n")
for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(
         field.name, field.type, field.length)
    txtFile.write(line)

txtFile.close()

print("Script completed")