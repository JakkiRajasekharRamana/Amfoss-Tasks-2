import os,shutil
from pathlib import Path
#p=os.path.abspath('some_folder')

for folderName,subfolders,filenames in os.walk('/home/rajasekhar/Test1'):
    #print('The current folder is ' + folderName)

    #for subfolder in subfolders:
    #    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if not (filename.endswith('.pdf') or filename.endswith('.jpg')):
            #print(filename)
            os.unlink(filename)
            #shutil.copytree('/home/rajasekhar/Test1/filename','/home/rajasekhar/some_folder')
        #print(filename)
        shutil.copytree('/home/rajasekhar/Test1','/home/rajasekhar/some_folder')
    print('')