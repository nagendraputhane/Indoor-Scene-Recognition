import xml.etree.ElementTree as ET
import glob
import os
import shutil
from os import path
from pathlib import Path

class ContinueI(Exception): #utility function to skip to outer loop
    pass

continue_i = ContinueI()

fileList = glob.glob("C:\\Users\\NAGENDRA\\Desktop\\ISR\\*\\*.xml") #list of annotation files

#f = open("C:\\Users\\NAGENDRA\\Desktop\\files.csv", "w+")

for eachFile in fileList:
    try: #to skip here after a file has been found with "person"
        tree = ET.parse(eachFile) #parse XML file
        root = tree.getroot()

        for elem in root:
            for subelem in elem: #parse through objects
                if "person" in subelem.text:
                    #f.write(eachFile)
                    #f.write('\n')

                    src = eachFile #annotations path

                    head, srcImgFile = path.split(src) #get file name
                    pre, ext = os.path.splitext(srcImgFile) #get extension
                    new_extension = '.jpg'
                    os.rename(srcImgFile, pre + new_extension) #rename extention
                    imgSrc = "C:\\JPEGImages\\" #folder that contains images
                    imageFolderName = os.path.basename(os.path.dirname(src)) #the folder heirarchy for Indoor Scene Recognition database
                    imgSrc = imgSrc + imageFolderName
                    Path(imgSrc).mkdir(parents=True, exist_ok=True) #create folder
                    imgSrc = imgSrc + srcImgFile #final images path

                    folderName = os.path.basename(os.path.dirname(src))
                    head, tail = path.split(src)
                    dst = "C:\\Users\\NAGENDRA\\Desktop\\new_b\\" + folderName + "\\" #new location for annotations
                    Path(dst).mkdir(parents=True, exist_ok=True)
                    dst = dst + tail #final annotations destination path

                    head, dstImgFile = path.split(dst)
                    pre, ext = os.path.splitext(dstImgFile)
                    new_extension = '.jpg'
                    os.rename(dstImgFile, pre + new_extension)
                    imgDst = "C:\\JPEGImages\\" #new location for images
                    imageFolderName = os.path.basename(os.path.dirname(src))
                    imgDst = imgDst + imageFolderName
                    Path(imgDst).mkdir(parents=True, exist_ok=True)
                    imgDst = imgDst + dstImgFile #final images destination path

                    shutil.copy(src, dst) #copy annotations
                    shutil.copy(imgSrc, imgDst) #copy images

                    raise continue_i
    except ContinueI:
        continue

#f.close()
