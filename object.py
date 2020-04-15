import xml.etree.ElementTree as ET
import glob
import os
import shutil
from os import path

class ContinueI(Exception):
    pass

continue_i = ContinueI()

fileList = glob.glob("C:\\Users\\NAGENDRA\\Desktop\\SUN\\*.xml")

f = open("C:\\Users\\NAGENDRA\\Desktop\\files.csv", "w+")

for eachFile in fileList:
    src = eachFile
    head, tail = path.split(src)
    dest = "C:\\Users\\NAGENDRA\\Desktop\\new_a\\" + tail
    try:
        tree = ET.parse(eachFile)
        root = tree.getroot()

        for elem in root:
            for subelem in elem:
                if "person" in subelem.text:
                    f.write(eachFile)
                    f.write('\n')
                    src = eachFile
                    head, tail = path.split(src)
                    dst = "C:\\Users\\NAGENDRA\\Desktop\\new_a\\" + tail
                    shutil.copy(src,dst)
                    raise continue_i
    except ContinueI:
        continue

f.close()
