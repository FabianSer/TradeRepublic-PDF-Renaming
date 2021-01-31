#pip install PyPDF4

from PyPDF4 import PdfFileReader
import shutil
import os
import re

def get_naming(file_name):
    pdfFile = open('./input/'+file_name, 'rb')
    pdfReader = PdfFileReader(pdfFile)
    pdfContent = pdfReader.getPage(0).extractText()
    pdfFile.close()
    ISIN = re.search(r"(?<=ISIN:)\s*(.*?)(?=\s)", pdfContent)
    DATUM = re.search(r"(?<=DATUM\n).*?(?=\n)", pdfContent)[0]
    DATUM_formatted = DATUM[-4:]+DATUM[3:5]+DATUM[:2]
    base = './output/' + DATUM_formatted + (('_'+ISIN[1]) if ISIN else '')
    if os.path.exists(base+'.pdf'):
        i = 1
        while os.path.exists(base+'_'+str(i)+'.pdf'):
            i += 1
        return base+'_'+str(i)+'.pdf'
    return base+'.pdf'


all_files = (os.listdir('./input/'))
all_files.remove('.gitkeep')

for file_name in all_files:
    new_file_name = get_naming(file_name)
    os.rename(r'./input/'+file_name, r'./input/'+new_file_name)
    shutil.move(r'./input/'+new_file_name, r'./output/'+new_file_name)
