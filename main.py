import os
import re
from shutil import copyfile

##### FUNCTION DEF #####
def getSongName(rootdir):
    songNames = []
    folderNames = []
    count = 0
    for it in os.scandir(rootdir):
        if it.is_dir():
            txt = it.path
            x = re.findall("(?=\d).*", txt)
            if(x):
                y = re.findall("[^\d\s].*", x[0])
                songNames.append(y)
                folderNames.append(txt)
                count += 1
            else:
                continue
    return(songNames,folderNames,count)

def getSongFile(rootdir):
    fullPath = []
    for filename in os.listdir(rootdir):
        if filename.endswith(".mp3") or filename.endswith(".MP3"):            
            pathToFile = os.path.join(rootdir, filename)
            fullPath.append(pathToFile)
            continue
        elif filename.endswith(".osu") or filename.endswith(".wav"):
            continue
        elif fullPath == []:
            return("error")
    return(fullPath[0])
##### END OF FUNCTION DEF #####

rootdir = input("Enter the path of the osu Songs directory: ")
destinationDir = input("Enter the path of the folder where you want to save your songs \n(Must be on the same drive as the osu folder): ")

nbSongs = getSongName(rootdir)[2]
for i in range(nbSongs):
    folderPath = ''.join(str(e) for e in getSongName(rootdir)[1][i])
    songString = ''.join(str(e) for e in getSongName(rootdir)[0][i])
    filePath = getSongFile(folderPath)
    if(filePath == "error"):
        continue
    else:
        copyfile(filePath, destinationDir+'\\'+songString+".mp3")