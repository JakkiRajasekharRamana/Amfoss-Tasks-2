import PyPDF2

text = open('dictionary.txt')
text = text.read()
text = text.split('\n')
pdf = open('watermarkencrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pdfWriter = PyPDF2.PdfFileWriter()
for i in text:
        if pdfReader.decrypt(i) == 1:
            print('Correct Password :D')
            print(i)
            break
        elif pdfReader.decrypt(i.lower()) == 1:
            print('Correct Password :D',)
            print(i)
            break
        else:
            print('Wrong Password')
