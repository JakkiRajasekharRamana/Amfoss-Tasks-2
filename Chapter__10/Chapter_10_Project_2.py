import os,shutil
from pathlib import Path
p=Path.home() 
for folderName,subfolders,filenames in os.walk('/home/rajasekhar/Test1'):
    #print('The current folder is ' + folderName)

    #for subfolder in subfolders:
    #    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        if(os.path.getsize(filename)>100):
            #print(filename)
            os.unlink(filename)
        #print('FILE INSIDE ' + folderName + ': '+ filename)
        print(filename)
    print('')