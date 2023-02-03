
import PyPDF2, os, re
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        #print(filename)
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.encrypt(input('Enter a password:'))
        filename = re.sub('_encrypted.pdf', '', filename)
        print('Deleting %s...' % (os.path.join(filename)))
        os.remove(os.path.join(filename + '.pdf'))

        #for pageNum in range(pdfReader.numPages):
        #    PageObj = pdfReader.getPage(pageNum)
        #pdf1Reader = PyPDF2.PdfFileReader(pdfFile)
        #print('YES')
for filename in os.listdir('.'):
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    if((pdfReader.isEncrypted)==True):
        x=pdfReader.decrypt(int(input('Enter Input:')))
        if(x==0 or x==False):
            print('incorrect')
