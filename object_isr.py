import xml.etree.ElementTree as ET
import glob
import os
import shutil
from os import path
from pathlib import Path

class ContinueI(Exception): #utility function to skip to outer loop
    pass

continue_i = ContinueI()

fileList = glob.glob("/home/internship_computervision/Nagendra/IndoorSceneRecognition/Annotations/*/*.xml")#ISR list of annotation files

for eachFile in fileList:
    try: #to skip here after a file has been found with "person"
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(eachFile, parser=parser) #parse XML file
        root = tree.getroot()

        for elem in root:
            for subelem in elem: #parse through objects
                if "person" in subelem.text:

                    src = eachFile #annotations path

                    head, srcImgFile = path.split(src) #get file name
                    pre, ext = os.path.splitext(srcImgFile) #get extension
                    new_extension = '.jpg'
                    imgSrc = "/home/internship_computervision/Nagendra/IndoorSceneRecognition/Images/" #folder that contains images
                    imageFolderName = os.path.basename(os.path.dirname(src)) #the folder heirarchy for Indoor Scene Recognition database
                    imgSrc = imgSrc + imageFolderName + "/"
                    Path(imgSrc).mkdir(parents=True, exist_ok=True) #create folder
                    imgSrc = imgSrc + pre + new_extension #final images path

                    folderName = os.path.basename(os.path.dirname(src))
                    head, tail = path.split(src)
                    dst = "/home/internship_computervision/Nagendra/PeopleIndoor/ISR/Annotations/" + folderName + "/" #new location for annotations
                    Path(dst).mkdir(parents=True, exist_ok=True)
                    dst = dst + tail #final annotations destination path

                    head, dstImgFile = path.split(dst)
                    pre, ext = os.path.splitext(dstImgFile)
                    new_extension = '.jpg'
                    imgDst = "/home/internship_computervision/Nagendra/PeopleIndoor/ISR/Images/" #new location for images
                    imageFolderName = os.path.basename(os.path.dirname(src))
                    imgDst = imgDst + imageFolderName + "/"
                    Path(imgDst).mkdir(parents=True, exist_ok=True)
                    imgDst = imgDst + pre + new_extension  #final images destination path

                    shutil.copy(src, dst) #copy annotations
                    shutil.copy(imgSrc, imgDst) #copy images

                    raise continue_i
    except ContinueI:
        continue

#f.close()
