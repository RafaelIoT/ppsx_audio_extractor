import os
import re
import sys
import time
import zipfile

from shutil import copyfile


"""

Como usar:

"""


class VoicePowerPoint:

    def __init__(self, filename):
        self.filename = filename
        self.zip = zipfile.ZipFile(filename)
        self.files = list()

    def searchAudioFiles(self):
        print(self.zip.filelist[1].filename)
        paths = self.zip.filelist


        print("Searching audio files....")

        for path in paths:
            if ".m4a" in path.filename:
                filename = path.filename.split("/")[-1]
                filenumber = int(re.findall(r'\d+', filename)[0])
                if len(self.files) < filenumber:
                    self.files.append(path)
                else:
                    self.files.insert(filenumber-1, path)

        time.sleep(1)
        print(self.filename +": "+ str(len(self.files))+" files found!")



    def mvToDir(self):
        dirPath = os.getcwd()+"/"+self.filename.split(".")[0]
        os.mkdir(dirPath)
        for f in self.files:
            filename = f.filename.split("/")[-1]
            filenumber = int(re.findall(r'\d+', filename)[0])
            filestr = str(filenumber)
            if filenumber < 10:
                filestr = "0"+str(filenumber)
            
            fileAudio = self.zip.open(f)

            audioFinal = open(dirPath+"/slide"+filestr+".m4a", "wb")
            audioFinal.write(fileAudio.read())
            audioFinal.close()


listdir = os.listdir()
print(listdir)
for f in listdir:
    if ".ppsx" in f:
        print(f)
        voicePP = VoicePowerPoint(f)
        voicePP.searchAudioFiles()
        voicePP.mvToDir()
        print(":..................")

