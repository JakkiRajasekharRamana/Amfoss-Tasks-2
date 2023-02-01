#! python3
# Import modules and write comments to describe this program.
import os
from PIL import Image
DRIVE_LOCATION=input('Enter hardrive location:')
if(DRIVE_LOCATION.startswith('C:\'')):
    for foldername, subfolders, filenames in os.walk(DRIVE_LOCATION):
        numPhotoFiles = 0
        numNonPhotoFiles = 0
        for filename in filenames:
        # Check if file extension isn't .png or .jpg.
            if (filename.endswith('.png') or filename.endswith('.jpg') ):
                numNonPhotoFiles += 1
                continue    # skip to next filename

        # Open image file using Pillow.
            width, height=filename.size 
        # Check if width & height are larger than 500.
            if(width >= 500 and height >= 500):
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
        if (filenames/2 < numNonPhotoFiles):
            print(pwd(foldername))
        else:
            print('More than half were not photos')
else:
    print('Please enter a valid directory')
