# -*- coding: utf-8 -*-
import arcpy

arcpy.env.workspace = r'C:\EsriTraining\PYTH\Running_scripts\Corvallis.gdb'#작업경로 설정
arcpy.env.overwriteOutput = True#덮어쓰기 세팅
# Buffer -> 기능, _analysis -> Toolbox의 별칭
arcpy.Buffer_analysis('Schools', "BuffSchools1000", '1000 feet')#C:\EsriTraining\PYTH\Running_scripts\Corvallis.gdb\Schools

print ("Script completed")
