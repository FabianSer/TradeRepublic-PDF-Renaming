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
    ISIN = re.search(r"(?<=ISIN: ).*?(?=\s)", pdfContent)[0]
    DATUM = re.search(r"(?<=DATUM\n).*?(?=\n)", pdfContent)[0]
    DATRUM_formatted = DATUM[-4:]+DATUM[3:5]+DATUM[:2]
    return ISIN+'_'+DATRUM_formatted+'.pdf'


all_files = (os.listdir('./input/'))

for file_name in all_files:
    new_file_name = get_naming(file_name)
    os.rename(r'./input/'+file_name, r'./input/'+new_file_name)
    shutil.move(r'./input/'+new_file_name, r'./output/'+new_file_name)
