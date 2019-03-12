from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os
dirfiles=os.listdir()
files=[]
for file in dirfiles:
    if file[-4:]=='.svg':
        files.append(file)
for file in files:
    drawing = svg2rlg(file)

    renderPM.drawToFile(drawing, file[:-4]+".png", fmt="PNG")
