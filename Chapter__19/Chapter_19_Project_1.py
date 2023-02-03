import os
from PIL import Image

#SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.PNG') or filename.endswith('.jpg') or filename.endswith('.JPG') or filename == LOGO_FILENAME or filename.endswith('.GIF') or filename.endswith('.BMG')):
        continue    

    im = Image.open(filename)
    width, height = im.size
    if width < 2*(logoWidth) and height < 2*(logoHeight):
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (logoWidth,logoHeight), logoIm)
        im.save(os.path.join('withLogo', filename))
    else:
        print('Logo has been skipped')
        break
#im.save(os.path.join('withLogo', filename))
