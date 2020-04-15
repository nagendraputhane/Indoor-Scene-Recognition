import xml.etree.ElementTree as ET
import glob
import os
import shutil
from os import path
from pathlib import Path

class ContinueI(Exception):
    pass

continue_i = ContinueI()

fileList = glob.glob("C:\\Users\\NAGENDRA\\Desktop\\ISR\\*\\*.xml")

f = open("C:\\Users\\NAGENDRA\\Desktop\\files.csv", "w+")

for eachFile in fileList:
    try:
        tree = ET.parse(eachFile)
        root = tree.getroot()

        for elem in root:
            for subelem in elem:
                if "person" in subelem.text:
                    f.write(eachFile)
                    f.write('\n')
                    src = eachFile
                    folderName = os.path.basename(os.path.dirname(src))
                    head, tail = path.split(src)
                    Path("/my/directory").mkdir(parents=True, exist_ok=True)
                    dst = "C:\\Users\\NAGENDRA\\Desktop\\new_b\\" + folderName + "\\"#+ tail
                    Path(dst).mkdir(parents=True, exist_ok=True)
                    dst = dst + tail
                    shutil.copy(src,dst)
                    raise continue_i
    except ContinueI:
        continue

f.close()
