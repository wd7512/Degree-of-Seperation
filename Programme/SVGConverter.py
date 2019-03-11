import cairosvg
import os
filesdir=os.listdir()
files=[]
for file in filesdir:
    if file[-4:]=='.svg':
        files.append(file)
for file in files:
    cairosvg.svg2pdf(url=file, write_to=file[:-4]+'.pdf')
