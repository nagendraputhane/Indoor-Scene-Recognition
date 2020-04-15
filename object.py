import xml.etree.ElementTree as ET
import glob

class ContinueI(Exception):
    pass

continue_i = ContinueI()

fileList = glob.glob("C:\\Users\\NAGENDRA\\Desktop\\SUN\\*.xml")

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
                    raise continue_i
    except ContinueI:
        continue

f.close()
