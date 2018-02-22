import os
from fixsvg_functions import indexmaker, fullmaker

folderlist= next(os.walk('.'))[1]

for folder in folderlist:
    for filen in os.listdir(folder + '/'):
        if filen.lower().endswith('.svg'):
            print filen
            indexmaker(folder,filen[:-4])
            fullmaker(folder,filen[:-4])
            print filen[:-4] + " converted to annotated diagram."