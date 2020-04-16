import xml.etree.ElementTree as ET
import glob
import os
import shutil
from os import path
from pathlib import Path

class ContinueI(Exception): #utility function to skip to outer loop
    pass

continue_i = ContinueI()

#list of annotation files
#ISR
#fileList = glob.glob("/home/internship_computervision/Nagendra/IndoorSceneRecognition/Annotations/*/*.xml")
#SUN
fileList = glob.glob("/home/internship_computervision/Nagendra/SUN2012pascalformat/Annotations/*.xml")

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
                    imgSrc = "/home/internship_computervision/Nagendra/SUN2012pascalformat/JPEGImages/"
                    imgSrc = imgSrc + pre + new_extension
                    #os.rename(src + srcImgFile, imgSrc + pre + new_extension) #rename extention
                    #imgSrc = "/home/internship_computervision/Nagendra/IndoorSceneRecognition/Images/" #folder that contains images
                    #imgSrc = "/home/internship_computervision/Nagendra/SUN2012pascalformat/JPEGImages/" #folder that contains images
                    #imageFolderName = os.path.basename(os.path.dirname(src)) #the folder heirarchy for Indoor Scene Recognition database
                    #imgSrc = imgSrc + imageFolderName
                    #Path(imgSrc).mkdir(parents=True, exist_ok=True) #create folder
                    #imgSrc = imgSrc + srcImgFile #final images path

                    folderName = os.path.basename(os.path.dirname(src))
                    head, tail = path.split(src)
                    dst = "/home/internship_computervision/Nagendra/PeopleIndoor/SUN/Annotations/"
                    #dst = "/home/internship_computervision/Nagendra/PeopleIndoor/ISR/Annotations/" + folderName + "/" #new location for annotations
                    #Path(dst).mkdir(parents=True, exist_ok=True)
                    dst = dst + tail #final annotations destination path

                    head, dstImgFile = path.split(dst)
                    pre, ext = os.path.splitext(dstImgFile)
                    new_extension = '.jpg'
                    imgDst = "/home/internship_computervision/Nagendra/PeopleIndoor/SUN/Images/"
                    imgDst = imgDst + pre + new_extension
                    #os.rename(dst + dstImgFile, imgDst + pre + new_extension)
                    #imgDst = "/home/internship_computervision/Nagendra/PeopleIndoor/SUN/Images/" #new location for images
                    #imgDst = "/home/internship_computervision/Nagendra/PeopleIndoor/ISR/Images/" #new location for images
                    #imageFolderName = os.path.basename(os.path.dirname(src))
                    #imgDst = imgDst + imageFolderName
                    #Path(imgDst).mkdir(parents=True, exist_ok=True)
                    #imgDst = imgDst + dstImgFile #final images destination path
                    #Path(imgDst).mkdir(parents=True, exist_ok=True)

                    shutil.copy(src, dst) #copy annotations
                    shutil.copy(imgSrc, imgDst) #copy images

                    raise continue_i
    except ContinueI:
        continue

#f.close()
