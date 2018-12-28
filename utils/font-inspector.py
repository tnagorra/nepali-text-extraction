import sys
from fontTools.ttLib import TTFont

ttf = TTFont(sys.argv[1], 0, verbose=0, allowVID=0,
             ignoreDecompileErrors=True,
             fontNumber=-1)

font_characters = {(y[0], chr(y[0]))
                   for x in ttf["cmap"].tables
                   for y in x.cmap.items()}

print(' '.join([x[1] for x in sorted(font_characters)]))
ttf.close()
